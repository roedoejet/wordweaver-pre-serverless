''' This is the API endpoint for Verbs
'''

from typing import List

from fastapi import APIRouter, HTTPException
from wordweaver.data import VERB_DATA
from wordweaver.models import Verb

router = APIRouter()

@router.get("/verbs", response_model=List[Verb], tags=["verbs"])
def read_verbs_from_file() -> List[Verb]:
    return VERB_DATA


@router.get("/verbs/{tag}", response_model=Verb, tags=["verbs"])
def read_verb_from_file_by_id(tag: str) -> Verb:
    for vb in VERB_DATA:
        if vb['tag'] == tag:
            return vb
    raise HTTPException(status_code=404, detail=f"Your search for '{tag}' returned no results")
