import json

with open('options.json') as f:
    data = json.load(f)

for i, item in enumerate(data):
    classes = [x for x in map(lambda x: x['type'], item['affixes'])]
    del data[i]['affixes']
    data[i]['classes'] = classes

with open('options-new.json', 'w') as f:
    f.write(json.dumps(data))