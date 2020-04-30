from wwapi.data import COUCHSERVER, USER, PASSWORD
import json
import requests


def find(db_name, selector):
    # This needs to be updated in the router
    headers = {'Content-type': 'application/json'}
    url = f'http://{USER}:{PASSWORD}@db:5984/{db_name}/_find'
    response = requests.post(url, data=json.dumps({'selector': selector}), headers=headers)
    return response.json()
