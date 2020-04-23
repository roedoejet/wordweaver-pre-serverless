''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Option

from wwapi.data.utils import find

router = APIRouter()


@router.get("/options", response_model=List[Option], tags=["options"])
def read_options() -> List[Option]:
    options = find({'data_type': 'option'})
    return options['docs']


@router.get("/options/{tag}", response_model=Option, tags=["options"])
def read_option_by_id(tag: str) -> Option:
    options = find({'data_type': 'option', 'tag': tag})
    return options['docs']
