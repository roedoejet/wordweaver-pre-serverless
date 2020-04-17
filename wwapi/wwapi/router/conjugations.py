''' This is the API endpoint for Conjugations
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Response

from wwapi.data.db import find

router = APIRouter()


@router.get("/conjugations", response_model=Response)
def read_conjugations(skip: int = 0, limit: int = 10, verb: List[str] = [], affopt: List[str] = [], agent: List[str] = [], patient: List[str] = []) -> Response:
    conjugations = find({'data_type': 'conjugation'})
    return conjugations['docs'][skip: skip + limit]
