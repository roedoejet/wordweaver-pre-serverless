''' Temporary static data until CouchDB integration
'''
import json
import os

import couchdb

DATA_PATH = os.path.dirname(__file__)

WWLANG = os.environ['WWLANG']

with open(os.path.join(DATA_PATH, WWLANG, 'options.json')) as f:
    OPTION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, 'pronouns.json')) as f:
    PRONOUN_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, 'verbs.json')) as f:
    VERB_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, 'conjugations.json')) as f:
    CONJUGATION_DATA = json.load(f)


USER = os.environ.get('COUCHDB_USER', '')
PASSWORD = os.environ.get('COUCHDB_PASSWORD', '')
COUCHSERVER = couchdb.Server('http://%s:%s@db:5984' % (USER, PASSWORD))
URL = f'http://{USER}:{PASSWORD}@db:5984'
