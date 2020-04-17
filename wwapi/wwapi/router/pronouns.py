''' This is the API endpoint for Pronouns
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Pronoun

from wwapi.data.utils import find

router = APIRouter()


@router.get("/pronouns", response_model=List[Pronoun], tags=["pronouns"])
def read_pronouns() -> List[Pronoun]:
    pns = find({'data_type': 'pronoun'})
    return pns['docs']


@router.get("/pronouns/{tag}", response_model=Pronoun, tags=["pronouns"])
def read_pronoun_by_id(tag: str) -> Pronoun:
    pns = find({'data_type': 'pronoun', 'tag': tag})
    return pns['docs']
