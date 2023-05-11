""" Temporary static data until CouchDB integration
"""
import gzip
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
# with open(os.path.join(DATA_PATH, WWLANG, "conjugations.json")) as f:
#     CONJUGATION_DATA = json.load(f)
CONJUGATION_DATA = []


def load_conjugation_data():
    """Deferred loading operation for CONJUGATION_DATA since it's big

    Call this method when you really need CONJUGATION_DATA to have been initialized.
    It's safe to call multiple times, it's a no-op if the data was already loaded."""
    global CONJUGATION_DATA
    if CONJUGATION_DATA == []:
        # We extend CONJUGATION_DATA rather than assign, to avoid invalidating
        # imports done elsewhere
        conj_file_name = os.path.join(DATA_PATH, WWLANG, "conjugations.json")
        try:
            # Read the uncompressed file if it exists
            with open(conj_file_name) as f:
                CONJUGATION_DATA.extend(json.load(f))
        except FileNotFoundError:
            # or the compressed one of the uncompressed one is not there.
            with gzip.open(os.path.join(DATA_PATH, WWLANG, "conjugations.json.gz"), "rt", encoding="utf-8") as f:
                CONJUGATION_DATA.extend(json.load(f))
