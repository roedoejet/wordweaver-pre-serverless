''' This is the API endpoint for Verbs
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Verb

from wwapi.data.utils import find

router = APIRouter()


@router.get("/verbs", response_model=List[Verb], tags=["verbs"])
def read_verbs() -> List[Verb]:
    verbs = find({'data_type': 'verb'})
    return verbs['docs']


@router.get("/verbs/{tag}", response_model=Verb, tags=["verbs"])
def read_verb_by_id(tag: str) -> Verb:
    verbs = find({'data_type': 'verb', 'tag': tag})
    return verbs['docs']
