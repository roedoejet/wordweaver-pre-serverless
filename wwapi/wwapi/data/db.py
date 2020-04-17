from wwapi.data import AFFIX_DATA, AFFIX_OPTION_DATA, VERB_DATA, PRONOUN_DATA
import requests
import json

def find(selector):
    headers = {'Content-type': 'application/json'}
    url = 'http://admin:password@db:5984/data/_find'
    response = requests.post(url, data=json.dumps({'selector': selector}), headers=headers)
    return response.json()
