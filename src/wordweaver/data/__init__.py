""" Temporary static data until CouchDB integration
"""
import json
import os

DEFAULT_LANG = "fr"

DATA_PATH = os.path.dirname(__file__)

WWLANG = os.environ.get("WWLANG", DEFAULT_LANG)

with open(os.path.join(DATA_PATH, WWLANG, "options.json")) as f:
    OPTION_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, "pronouns.json")) as f:
    PRONOUN_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, "verbs.json")) as f:
    VERB_DATA = json.load(f)
with open(os.path.join(DATA_PATH, WWLANG, "conjugations.json")) as f:
    CONJUGATION_DATA = json.load(f)
