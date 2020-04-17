''' This is the API endpoint for Conjugations
'''

from typing import List

from fastapi import APIRouter, Query, HTTPException

from wwapi.models import Response

from wwapi.data.utils import find

router = APIRouter()


def create_selector(affopt, agent, patient):
    return {'affopt': affopt, }


@router.get("/conjugations", response_model=Response, tags=["conjugations"])
def read_conjugations(root: List[str] = Query(None), affopt: List[str] = Query(None),
                      agent: List[str] = Query(None), patient: List[str] = Query(None)) -> Response:
    input_selector = {}
    if root:
        input_selector['root'] = {'$in': root}
    if affopt:
        input_selector['affopt'] = {'$in': affopt}
    if agent:
        input_selector['agent'] = {'$in': agent}
    if patient:
        input_selector['patient'] = {'$in': patient}
    if root or affopt or agent or patient:
        selector = {'data_type': 'conjugation', 'input': input_selector}
    else:
        selector = {'data_type': 'conjugation'}
    conjugations = find(selector)
    if conjugations['docs']:
        return conjugations['docs']
    else:
        raise HTTPException(status_code=404, detail="Your search returned no results")