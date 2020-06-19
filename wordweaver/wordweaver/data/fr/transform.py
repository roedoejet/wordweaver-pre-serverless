import json
from copy import deepcopy

with open('conjugations.json') as f:
    data = json.load(f)
new_data = []
for conjugation in data:
    if isinstance(conjugation['input']['agent'], list):
        for agent in conjugation['input']['agent']:
            new_conjugation = deepcopy(conjugation)
            new_conjugation['input']['agent'] = agent
            new_data.append(new_conjugation)
    else:
        new_data.append(conjugation)
        
with open('conjugations1.json', 'w') as f:
    json.dump(new_data, f)