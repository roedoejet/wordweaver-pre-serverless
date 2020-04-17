''' Temporary static data until CouchDB integration
'''
import json
import os

DATA_PATH = os.path.dirname(__file__)

with open(os.path.join(DATA_PATH, 'affixes.json')) as f:
    AFFIX_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'affix_options.json')) as f:
    AFFIX_OPTION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'pronouns.json')) as f:
    PRONOUN_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'verbs.json')) as f:
    VERB_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'conjugations.json')) as f:
    CONJUGATION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, 'tiers.json')) as f:
    TIER_DATA = json.load(f)