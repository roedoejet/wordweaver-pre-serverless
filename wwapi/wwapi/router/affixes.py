''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Affix, AffixOption
# Data
from wwapi.data import AFFIX_DATA, AFFIX_OPTION_DATA

from wwapi.data.db import find

router = APIRouter()


@router.get("/affixes", response_model=List[Affix])
def read_affixes() -> List[Affix]:
    affixes = find({'data_type': 'affix'})
    return affixes['docs']


@router.get("/affix-options", response_model=List[AffixOption])
def read_affix_options() -> List[AffixOption]:
    affix_options = find({'data_type': 'affopt'})
    return affix_options['docs']
