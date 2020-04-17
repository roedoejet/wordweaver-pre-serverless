''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Affix, AffixOption

from wwapi.data.db import find

router = APIRouter()


@router.get("/affixes", response_model=List[Affix])
def read_affixes() -> List[Affix]:
    affixes = find({'data_type': 'affix'})
    return affixes['docs']

@router.get("/affixes/{tag}", response_model=Affix)
def read_affix_by_id(tag: str) -> Affix:
    affixes = find({'data_type': 'affix', 'tag': tag})
    return affixes['docs']

@router.get("/affix-options", response_model=List[AffixOption])
def read_affix_options() -> List[AffixOption]:
    affix_options = find({'data_type': 'affopt'})
    return affix_options['docs']

@router.get("/affix-options/{tag}", response_model=AffixOption)
def read_affopt_by_id(tag: str) -> AffixOption:
    affix_options = find({'data_type': 'affopt', 'tag': tag})
    return affix_options['docs']