import couchdb
from wwapi.data import AFFIX_DATA, AFFIX_OPTION_DATA, PRONOUN_DATA, VERB_DATA, CONJUGATION_DATA
from wwapi.models import Affix, AffixOption, Pronoun, Verb, ResponseObject

user = 'admin'
password = 'password'
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

data_db = 'data'

del couchserver[data_db]
db = couchserver.create(data_db)

for affix in AFFIX_DATA:
    test = Affix(**affix)
    affix = test.dict()
    affix['data_type'] = 'affix'
    db.save(affix)

for affix_option in AFFIX_OPTION_DATA:
    test = AffixOption(**affix_option)
    affix_option = test.dict()
    affix_option['data_type'] = 'affopt'
    db.save(affix_option)

for pronoun in PRONOUN_DATA:
    test = Pronoun(**pronoun)
    pronoun = test.dict()
    pronoun['data_type'] = 'pronoun'
    db.save(pronoun)

for verb in VERB_DATA:
    test = Verb(**verb)
    verb = test.dict()
    verb['data_type'] = 'verb'
    db.save(verb)

for conjugation in CONJUGATION_DATA:
    test = ResponseObject(**conjugation)
    conjugation = test.dict()
    conjugation['data_type'] = 'conjugation'
    db.save(conjugation)
