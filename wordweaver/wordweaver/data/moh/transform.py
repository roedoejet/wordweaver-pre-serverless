import json
from copy import deepcopy

with open('verbs.json') as f:
    verb_data = json.load(f)

with open("i18n/en.json") as f:
    en_data = json.load(f)

with open('i18n/moh.json') as f:
    moh_data = json.load(f)

for verb in verb_data:
    en_data['ww-data']['verbs'][verb['tag']] = verb['gloss']
    moh_data['ww-data']['verbs'][verb['tag']] = verb['display']

with open('en.json', 'w') as f:
    json.dump(en_data, f)

with open('moh.json', 'w') as f:
    json.dump(moh_data, f)