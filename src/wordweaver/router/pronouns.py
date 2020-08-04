''' This is the API endpoint for pronouns
'''

from typing import List

from fastapi import APIRouter, HTTPException
from wordweaver.data import PRONOUN_DATA
from wordweaver.models import Pronoun

router = APIRouter()

@router.get("/pronouns", response_model=List[Pronoun], tags=["pronouns"])
def read_pronouns_from_file() -> List[Pronoun]:
    return PRONOUN_DATA


@router.get("/pronouns/{tag}", response_model=Pronoun, tags=["pronouns"])
def read_pronoun_from_file_by_id(tag: str) -> Pronoun:
    for pronoun in PRONOUN_DATA:
        if pronoun['tag'] == tag:
            return pronoun
    raise HTTPException(status_code=404, detail=f"Your search for '{tag}' returned no results")
