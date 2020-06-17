# -*- coding: utf-8 -*-
from wordweaver.data import OPTION_DATA, CONJUGATION_DATA, VERB_DATA, PRONOUN_DATA, DATA_PATH, WWLANG
from wordweaver.models import Option, Pronoun, Verb, ResponseObject
from tqdm import tqdm
from loguru import logger
from pydantic.error_wrappers import ValidationError
from pprint import pformat
import sys
import os
import requests
import json
from pathlib import Path
import gzip
from importlib import import_module

fmt = "\n <level>WordWeaver</level> | <green>{function}</green> | {message} \n"
logger.remove()
logger.add(sys.stderr, format=fmt, colorize=True)

def validate():
    # Shared messages
    CHECKING = "Checking {} {}..."
    ERROR = "Uh oh! not all of your {} matched the declared type. \nYour tier looks like this:\n\n {}\n\n but we expected: \n\n{}"
    # Check Options
    logger.info(CHECKING.format(len(OPTION_DATA), 'options'))
    for option in tqdm(OPTION_DATA):
        try:
            Option.validate(option)
        except ValidationError:
            logger.error(ERROR.format('options', pformat(option),
                                      pformat(Option.schema()['properties'])))
            return
    # Check Pronouns
    logger.info(CHECKING.format(len(PRONOUN_DATA), 'pronouns'))
    for pronoun in tqdm(PRONOUN_DATA):
        try:
            Pronoun.validate(pronoun)
        except ValidationError:
            logger.error(ERROR.format('pronouns', pformat(pronoun),
                                      pformat(Pronoun.schema()['properties'])))
            return
    # Check Verbs
    logger.info(CHECKING.format(len(VERB_DATA), 'verbs'))
    for verb in tqdm(VERB_DATA):
        try:
            Verb.validate(verb)
        except ValidationError:
            logger.error(ERROR.format('verbs', pformat(verb),
                                      pformat(Verb.schema()['properties'])))
            return
    # Check Conjugations
    logger.info(CHECKING.format(len(CONJUGATION_DATA), 'conjugations'))
    for conjugation in tqdm(CONJUGATION_DATA):
        try:
            ResponseObject.validate(conjugation)
        except ValidationError:
            logger.error(ERROR.format('conjugations', pformat(
                conjugation), pformat(ResponseObject.schema()['properties'])))
            return
    logger.info("Success! All data checked")


def gzip_assets():
    """ This function gzips all of your json data to intialize it for your WordWeaver. This is the recommended method
    """
    logger.info("Starting to optimize and gzip assets")
    p = Path(os.path.join(DATA_PATH, WWLANG))
    for fn in tqdm(p.glob('*.json')):
        logger.info(f"Optimizing and gzipping '{fn.name}'")
        # if fn.stat().st_size > 1400:
        file_path = str(fn)
        with open(file_path) as f:
            data = json.load(f)

        if 'conjugations.json' == fn.name:
            longest = 0
            longest_key = 'root'
            for k, v in data[0]['input'].items():
                if len(v) >= longest:
                    longest = len(v)
                    longest_key = k   
            data.sort(key=lambda o: o["input"][longest_key], reverse=True)
            assert all(set(o.keys()) == {"input", "output"} for o in data)

        with gzip.open(file_path + '.gz', 'wt') as zipfile:
            json.dump(data, zipfile, separators=(",",":"), ensure_ascii=False, sort_keys=True)


def create_protobufs():
    protocmodule = import_module(f'wordweaver.data.{WWLANG}.conjugations_pb2')
    with open(os.path.join(DATA_PATH, WWLANG, 'conjugations.json')) as f:
        data = json.load(f)
    # Response
    protobuf_data = protocmodule.Response()
    for conjugation in data:
        # Object
        response_object = protobuf_data.response.add()
        # Input
        input_object = protocmodule.ConjugationInput(**conjugation['input'])
        response_object.input.CopyFrom(input_object)
        # Output
        for item in conjugation['output']:
            # Morpheme
            morpheme = response_object.output.morphemes.add()
            morpheme.CopyFrom(protocmodule.ResponseMorpheme(**item))
    with open('test.protobuf', 'wb') as zipfile:
        zipfile.write(protobuf_data.SerializeToString())
    with gzip.open('test.protobuf.gz', 'wb') as zipfile:
        zipfile.write(protobuf_data.SerializeToString())
