# -*- coding: utf-8 -*-
from wwapi.data import OPTION_DATA, CONJUGATION_DATA, VERB_DATA, PRONOUN_DATA
from wwapi.models import Option, Pronoun, Verb, ResponseObject
import requests
import json
import couchdb
from tqdm import tqdm
from loguru import logger
from pydantic.error_wrappers import ValidationError
from pprint import pformat
import sys

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

    user = 'admin'
    password = 'password'
    couchserver = couchdb.Server("http://%s:%s@db:5984/" % (user, password))

    data_db = 'data'
    logger.warning(f"Deleting {data_db} database")
    if data_db in couchserver:
        del couchserver[data_db]
    db = couchserver.create(data_db)

    for option in OPTION_DATA:
        option['data_type'] = 'option'
        db.save(option)

    for pronoun in PRONOUN_DATA:
        pronoun['data_type'] = 'pronoun'
        db.save(pronoun)

    for verb in VERB_DATA:
        verb['data_type'] = 'verb'
        db.save(verb)

    for conjugation in CONJUGATION_DATA:
        conjugation['data_type'] = 'conjugation'
        db.save(conjugation)

    logger.info("Success! All data initialized into Database")


def find(selector):
    headers = {'Content-type': 'application/json'}
    url = 'http://admin:password@db:5984/data/_find'
    response = requests.post(url, data=json.dumps(
        {'selector': selector}), headers=headers)
    return response.json()


if __name__ == '__main__':
    initialize_db()
