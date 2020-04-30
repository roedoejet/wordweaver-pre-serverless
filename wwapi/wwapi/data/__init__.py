''' Temporary static data until CouchDB integration
'''
import json
import os

import couchdb

DATA_PATH = os.path.dirname(__file__)

LANG_CODE = "fr"

with open(os.path.join(DATA_PATH, LANG_CODE, 'options.json')) as f:
    OPTION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, LANG_CODE, 'pronouns.json')) as f:
    PRONOUN_DATA = json.load(f)
with open(os.path.join(DATA_PATH, LANG_CODE, 'verbs.json')) as f:
    VERB_DATA = json.load(f)
with open(os.path.join(DATA_PATH, LANG_CODE, 'conjugations.json')) as f:
    CONJUGATION_DATA = json.load(f)

USER = os.environ['COUCHDB_USER']
PASSWORD = os.environ['COUCHDB_PASSWORD']
COUCHSERVER = couchdb.Server('http://%s:%s@db:5984' % (USER, PASSWORD))
URL = f'http://{USER}:{PASSWORD}@db:5984'
