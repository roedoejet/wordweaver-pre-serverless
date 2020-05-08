# -*- coding: utf-8 -*-
from wwapi.data import OPTION_DATA, CONJUGATION_DATA, VERB_DATA, PRONOUN_DATA, USER, PASSWORD, COUCHSERVER, URL
from wwapi.models import Option, Pronoun, Verb, ResponseObject
from tqdm import tqdm
from loguru import logger
from pydantic.error_wrappers import ValidationError
from pprint import pformat
import sys
import requests
import json

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


def initialize_db():
    validate()
    UPDATE_LIMIT = 10000
    data_db = 'data'
    verb_db = 'verb'
    pronoun_db = 'pronoun'
    option_db = 'option'
    dbs = [data_db, verb_db, pronoun_db, option_db]
    db_data = {data_db: CONJUGATION_DATA, verb_db: VERB_DATA,
               pronoun_db: PRONOUN_DATA, option_db: OPTION_DATA}
    for db_name in dbs:
        logger.warning(f"Deleting '{db_name}' database")
        # Start fresh, delete old data
        if db_name in COUCHSERVER:
            del COUCHSERVER[db_name]
        db = COUCHSERVER.create(db_name)
        # Bulk upload docs
        if len(db_data[db_name]) > UPDATE_LIMIT:
            data_length = len(db_data[db_name])
            logger.info(f"Whoa, you've got a lot of data here, we're going to have to split it up. This might take a while.")
            counter = 1
            while (counter * UPDATE_LIMIT) < data_length:
                start = (counter - 1) * UPDATE_LIMIT
                end = counter * UPDATE_LIMIT
                logger.info(f"Adding documents from {start} to {end} to '{db_name}' database")
                db.update(db_data[db_name][start:end])
                counter += 1
            logger.info(f"Adding documents from {end} to {data_length} to '{db_name}' database")
            db.update(db_data[db_name][end:])
        else:
            db.update(db_data[db_name])
        # Initialize view by tag
        # if db_name in [verb_db, pronoun_db, option_db]:
        #     # Add indices for tags
        #     headers = {'Content-type': 'application/json'}
        #     url = f'{URL}/{db_name}/_index'
        #     index = {
        #         "index": {
        #             "fields": [
        #                 "tag"
        #             ]
        #         },
        #         "name": "tag-json-index",
        #         "type": "json"
        #     }
        #     requests.post(url, data=json.dumps(index), headers=headers)
        if db_name == data_db:
            # Add indices for root by default
            headers = {'Content-type': 'application/json'}
            url = f'{URL}/{db_name}/_index'
            index = {
                "index": {
                    "fields": [
                        "input.root"
                    ]
                },
                "name": "tag-json-index",
                "type": "json"
            }
            requests.post(url, data=json.dumps(index), headers=headers)

    logger.info("Success! All data initialized into CouchDB Database")


if __name__ == '__main__':
    initialize_db()
