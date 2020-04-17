import couchdb
from wwapi.data import AFFIX_DATA, AFFIX_OPTION_DATA, PRONOUN_DATA, VERB_DATA, CONJUGATION_DATA

user = 'admin'
password = 'password'
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

data_db = 'data'

db = couchserver.create(data_db)

for affix in AFFIX_DATA:
    affix['data_type'] = 'affix'
    db.save(affix)

for affix_option in AFFIX_OPTION_DATA:
    affix_option['data_type'] = 'affopt'
    db.save(affix_option)

for pronoun in PRONOUN_DATA:
    pronoun['data_type'] = 'pronoun'
    db.save(pronoun)

for verb in VERB_DATA:
    verb['data_type'] = 'verb'
    db.save(verb)

for conjugation in CONJUGATION_DATA:
    conjugation['data_type'] = 'conjugation'
    db.save(conjugation)
