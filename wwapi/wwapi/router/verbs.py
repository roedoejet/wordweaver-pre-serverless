''' This is the API endpoint for Verbs
'''

from typing import List

from fastapi import APIRouter, Response, status, HTTPException

from wwapi.models import Verb

from wwapi.router.utils import find

router = APIRouter()

DB_NAME = 'verb'


@router.get("/verbs", response_model=List[Verb], tags=["verbs"])
def read_verbs() -> List[Verb]:
    selector = {
        "tag": {
            "$gt": 0
        }
    }
    verbs = find(DB_NAME, selector)['docs']
    return verbs


@router.get("/verbs/{tag}", response_model=Verb, tags=["verbs"])
def read_verb_by_id(tag: str, response: Response) -> Verb:
    selector = {
        "tag": tag
    }
    verbs = find(DB_NAME, selector)['docs']
    if len(verbs) > 1:
        response.status_code = status.HTTP_206_PARTIAL_CONTENT
    if len(verbs) < 1:
        raise HTTPException(
            status_code=404, detail="Your search returned no results")
    return verbs[0]
