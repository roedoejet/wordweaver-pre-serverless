''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Affix, AffixOption

from wwapi.data.utils import find

router = APIRouter()


@router.get("/affixes", response_model=List[Affix], tags=["affixes"])
def read_affixes() -> List[Affix]:
    affixes = find({'data_type': 'affix'})
    return affixes['docs']

@router.get("/affixes/{tag}", response_model=Affix, tags=["affixes"])
def read_affix_by_id(tag: str) -> Affix:
    affixes = find({'data_type': 'affix', 'tag': tag})
    return affixes['docs']

@router.get("/options", response_model=List[AffixOption], tags=["affixes"])
def read_affix_options() -> List[AffixOption]:
    affix_options = find({'data_type': 'option'})
    return affix_options['docs']

@router.get("/options/{tag}", response_model=AffixOption, tags=["affixes"])
def read_option_by_id(tag: str) -> AffixOption:
    affix_options = find({'data_type': 'option', 'tag': tag})
    return affix_options['docs']