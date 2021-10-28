# -*- coding: utf-8 -*-
import gzip
import json
import os
import sys
from importlib import import_module
from pathlib import Path
from pprint import pformat

from loguru import logger
from pydantic.error_wrappers import ValidationError
from tqdm import tqdm
from wordweaver.data import (
    CONJUGATION_DATA,
    DATA_PATH,
    OPTION_DATA,
    PRONOUN_DATA,
    VERB_DATA,
    WWLANG,
)
from wordweaver.models import Option, Pronoun, ResponseObject, Verb

fmt = "\n <level>WordWeaver</level> | <green>{function}</green> | {message} \n"
logger.remove()
logger.add(sys.stderr, format=fmt, colorize=True)


def validate_data():
    # Shared messages
    CHECKING = "Checking {} {}..."
    ERROR = """Uh oh! not all of your {} matched the declared type.
    \nYour tier looks like this:\n\n {}\n\n but we expected: \n\n{}"""
    any_errors = False
    # Check Options
    logger.info(CHECKING.format(len(OPTION_DATA), "options"))
    for option in tqdm(OPTION_DATA):
        try:
            Option.validate(option)
        except ValidationError:
            logger.error(
                ERROR.format(
                    "options", pformat(option), pformat(Option.schema()["properties"])
                )
            )
            any_errors = True
            continue
    # Check Pronouns
    logger.info(CHECKING.format(len(PRONOUN_DATA), "pronouns"))
    for pronoun in tqdm(PRONOUN_DATA):
        try:
            Pronoun.validate(pronoun)
        except ValidationError:
            logger.error(
                ERROR.format(
                    "pronouns",
                    pformat(pronoun),
                    pformat(Pronoun.schema()["properties"]),
                )
            )
            any_errors = True
            continue
    # Check Verbs
    logger.info(CHECKING.format(len(VERB_DATA), "verbs"))
    for verb in tqdm(VERB_DATA):
        try:
            Verb.validate(verb)
        except ValidationError:
            logger.error(
                ERROR.format(
                    "verbs", pformat(verb), pformat(Verb.schema()["properties"])
                )
            )
            any_errors = True
            continue
    # Check Conjugations
    logger.info(CHECKING.format(len(CONJUGATION_DATA), "conjugations"))
    for conjugation in tqdm(CONJUGATION_DATA):
        try:
            ResponseObject.validate(conjugation)
        except ValidationError:
            logger.error(
                ERROR.format(
                    "conjugations",
                    pformat(conjugation),
                    pformat(ResponseObject.schema()["properties"]),
                )
            )
            any_errors = True
            continue
    if not any_errors:
        logger.info("Success! All data checked")
    else:
        logger.error(
            "Uh oh! Not all data passed the checks, please look at logged output above for more information."
        )


def gzip_assets():
    """This function gzips all of your json data."""
    logger.info("Starting to optimize and gzip assets")
    p = Path(os.path.join(DATA_PATH, WWLANG))
    for fn in tqdm(list(p.glob("*.json")) + list(p.glob("i18n/*.json"))):
        logger.info(f"Optimizing and gzipping '{fn.name}'")
        # if fn.stat().st_size > 1400:
        file_path = str(fn)
        with open(file_path) as f:
            data = json.load(f)

        if "conjugations.json" == fn.name:
            longest = 0
            longest_key = "root"
            for k, v in data[0]["input"].items():
                if len(v) >= longest:
                    longest = len(v)
                    longest_key = k
            data.sort(key=lambda o: o["input"][longest_key], reverse=True)
            assert all(set(o.keys()) == {"input", "output"} for o in data)

        with gzip.open(file_path + ".gz", "wt") as zipfile:
            json.dump(
                data, zipfile, separators=(",", ":"), ensure_ascii=False, sort_keys=True
            )


def create_protobufs():
    protocmodule = import_module(f"wordweaver.data.{WWLANG}.conjugations_pb2")
    with open(os.path.join(DATA_PATH, WWLANG, "conjugations.json")) as f:
        data = json.load(f)
    # Response
    protobuf_data = protocmodule.Response()
    for conjugation in data:
        # Object
        response_object = protobuf_data.response.add()
        # Input
        input_object = protocmodule.ConjugationInput(**conjugation["input"])
        response_object.input.CopyFrom(input_object)
        # Output
        for item in conjugation["output"]:
            # Morpheme
            morpheme = response_object.output.morphemes.add()
            morpheme.CopyFrom(protocmodule.ResponseMorpheme(**item))
    with open("test.protobuf", "wb") as zipfile:
        zipfile.write(protobuf_data.SerializeToString())
    with gzip.open("test.protobuf.gz", "wb") as zipfile:
        zipfile.write(protobuf_data.SerializeToString())


def i18n_extract(langs, **kwargs):
    logger.info(f"Extracting translations for {WWLANG}")
    default = None
    i18n_path = os.path.join(DATA_PATH, WWLANG, "i18n")
    if not os.path.exists(i18n_path):
        os.mkdir(i18n_path)
    # Extract all tags
    if default is None:
        options = {
            item["tag"]: f"ww-data.options.items.{item['tag']}" for item in OPTION_DATA
        }
        option_types = {
            item["type"]: f"ww-data.options.types.{item['type']}"
            for item in OPTION_DATA
            if "type" in item
        }
        agents = {
            item["tag"]: f"ww-data.pronouns.agents.{item['tag']}"
            for item in PRONOUN_DATA
        }
        patients = {
            item["tag"]: f"ww-data.pronouns.patients.{item['tag']}"
            for item in PRONOUN_DATA
        }
        verbs = {item["tag"]: f"ww-data.verbs.{item['tag']}" for item in VERB_DATA}
    else:
        options = {item["tag"]: default for item in OPTION_DATA}
        option_types = {item["type"]: default for item in OPTION_DATA if "type" in item}
        agents = {item["tag"]: default for item in PRONOUN_DATA}
        patients = agents
        verbs = {item["tag"]: default for item in VERB_DATA}
    i18n_data = {
        "ww-data": {
            "options": {"items": options, "types": option_types},
            "pronouns": {"agents": agents, "patients": patients},
            "verbs": verbs,
        }
    }

    # Update each existing lang, and write new ones
    for lang in tqdm([lg for lg in langs]):
        logger.info(f"Processing translations for '{lang}'")
        lang_path = os.path.join(i18n_path, lang + ".json")
        if os.path.exists(lang_path):
            logger.info(f"Translations exist for '{lang}', attempting to merge")
            with open(lang_path) as f:
                lang_data = json.load(f)
            if kwargs["force"]:
                logger.warning("Force overriding existing translations")
                lang_data = {**lang_data, **i18n_data}
            else:
                logger.info("Merging with existing translations.")
                lang_data = {**i18n_data, **lang_data}
        else:
            logger.info(
                f"""Translations do not exist for '{lang}',
                attempting to create new file"""
            )
            lang_data = i18n_data
        with open(lang_path, "w") as f:
            json.dump(lang_data, f)
    logger.info(
        """Process finished. Please review your translations.
        Then add them to your assets by using 'wordweaver add-translations'"""
    )


def i18n_add(langs, **kwargs):

    logger.info(f"Adding translations for {WWLANG}")
    assets = ["pronouns", "options", "verbs"]
    if kwargs["assets"]:
        assets = [a for a in kwargs["assets"]]
    assets_path = os.path.join(DATA_PATH, WWLANG)
    i18n_path = os.path.join(assets_path, "i18n")
    for lang in [lg for lg in langs]:
        with open(os.path.join(i18n_path, lang + ".json")) as f:
            i18n_data = json.load(f)
        for asset in assets:
            with open(os.path.join(assets_path, asset + ".json")) as f:
                asset_data = json.load(f)
            if asset == "verbs":
                for k, v in tqdm(i18n_data["ww-data"]["verbs"].items()):
                    for verb in asset_data:
                        if verb["tag"] == k:
                            verb[lang] = v
            elif asset == "options":
                types = i18n_data["ww-data"]["options"]["types"]
                for k, v in tqdm(types.items()):
                    for option in asset_data:
                        if option["type"] == k:
                            if lang not in option:
                                option[lang] = {}
                            option[lang]["type"] = v
                items = i18n_data["ww-data"]["options"]["items"]
                for k, v in tqdm(items.items()):
                    for option in asset_data:
                        if option["tag"] == k:
                            if lang not in option:
                                option[lang] = {}
                            option[lang]["tag"] = v
            elif asset == "pronouns":
                agents = i18n_data["ww-data"]["pronouns"]["agents"]
                for k, v in tqdm(agents.items()):
                    for pn in asset_data:
                        if pn["tag"] == k:
                            if lang not in pn:
                                pn[lang] = {}
                            pn[lang]["agent"] = v
                patients = i18n_data["ww-data"]["pronouns"]["patients"]
                for k, v in tqdm(patients.items()):
                    for pn in asset_data:
                        if pn["tag"] == k:
                            if lang not in pn:
                                option[lang] = {}
                            pn[lang]["patient"] = v
            logger.info(f"Writing translated data to {asset}")
            with open(os.path.join(assets_path, asset + ".json"), "w") as f:
                json.dump(asset_data, f)
