''' This is the API endpoint for Pronouns
'''

from typing import List

from fastapi import APIRouter, Response, status, HTTPException

from wwapi.models import Pronoun

from wwapi.router.utils import find

router = APIRouter()

DB_NAME = 'pronoun'

@router.get("/pronouns", response_model=List[Pronoun], tags=["pronouns"])
def read_pronouns() -> List[Pronoun]:
    selector = {
        "tag": {
            "$gt": 0
        }
    }
    pns = find(DB_NAME, selector)['docs']
    return pns


@router.get("/pronouns/{tag}", response_model=Pronoun, tags=["pronouns"])
def read_pronoun_by_id(tag: str, response: Response) -> Pronoun:
    selector = {
        "tag": tag
    }
    pns = find(DB_NAME, selector)['docs']
    if len(pns) > 1:
        response.status_code = status.HTTP_206_PARTIAL_CONTENT
    if len(pns) < 1:
        raise HTTPException(
            status_code=404, detail="Your search returned no results")
    return pns[0]
