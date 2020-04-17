''' This is the API endpoint for Pronouns
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Pronoun

from wwapi.data.db import find

router = APIRouter()


@router.get("/pronouns", response_model=List[Pronoun])
def read_pronouns() -> List[Pronoun]:
    pns = find({'data_type': 'pronoun'})
    return pns['docs']


@router.get("/pronouns/{tag}", response_model=Pronoun)
def read_pronoun_by_id(tag: str) -> Pronoun:
    pns = find({'data_type': 'pronoun', 'tag': tag})
    return pns['docs']
