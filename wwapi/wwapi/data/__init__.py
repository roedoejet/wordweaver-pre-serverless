''' Temporary static data until CouchDB integration
'''
import json
import os

import couchdb

DATA_PATH = os.path.dirname(__file__)

with open(os.path.join(DATA_PATH, 'options.json')) as f:
    OPTION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'pronouns.json')) as f:
    PRONOUN_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'verbs.json')) as f:
    VERB_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'conjugations.json')) as f:
    CONJUGATION_DATA = json.load(f)

USER = 'admin'
PASSWORD = 'password'
COUCHSERVER = couchdb.Server('http://%s:%s@db:5984' % (USER, PASSWORD))
URL = f'http://{USER}:{PASSWORD}@db:5984'
