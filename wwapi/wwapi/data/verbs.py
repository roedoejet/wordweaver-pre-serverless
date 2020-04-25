import json

with open('verbs.json') as f:
    data = json.load(f)

for i, item in enumerate(data):
    classes = []
    if item['tag'][-2:] == '-r':
        classes = ['red', 'color-red']
    elif item['tag'][-2:] == '-b':
        classes = ['blue', 'color-blue']
    elif item['tag'][-2:] == '-p':
        classes = ['purple', 'color-purple']
    data[i]['classes'] = classes

with open('verbs-new.json', 'w') as f:
    f.write(json.dumps(data))
