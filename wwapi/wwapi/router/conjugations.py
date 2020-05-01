''' This is the API endpoint for Conjugations
'''

from typing import List

from fastapi import APIRouter, Query, HTTPException, Response as FAResponse

from wwapi.models import Response

from wwapi.router.utils import find

router = APIRouter()

DB_NAME = 'data'


def return_selector(arg):
    if not arg:
        return False
    if len(arg) == 1:
        return arg[0]
    else:
        return {"$in": arg}


@router.get("/conjugations", response_model=Response, tags=["conjugations"])
def read_conjugations(response: FAResponse, root: List[str] = Query(None), option: List[str] = Query(None),
                      agent: List[str] = Query(None), patient: List[str] = Query(None)) -> Response:
    selector = {}
    agent = return_selector(agent)
    patient = return_selector(patient)
    option = return_selector(option)
    conjugations = []
    # Queries have to be joined because for some un-relaxing reason,
    # CouchDB queries with $in or $or do not actually use indices
    if root:
        for root_tag in root:
            selector['input.root'] = root_tag
            if option:
                selector['input.option'] = option
            if agent:
                selector['input.agent'] = agent
            if patient:
                selector['input.patient'] = patient
            conjugations += find(DB_NAME, selector)['docs']
    return conjugations
