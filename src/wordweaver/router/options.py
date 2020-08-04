''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter, HTTPException

from wordweaver.data import OPTION_DATA
from wordweaver.models import Option

router = APIRouter()

@router.get("/options", response_model=List[Option], tags=["options"])
def read_options_from_file() -> List[Option]:
    return OPTION_DATA


@router.get("/options/{tag}", response_model=Option, tags=["options"])
def read_option_from_file_by_id(tag: str) -> Option:
    for option in OPTION_DATA:
        if option['tag'] == tag:
            return option
    raise HTTPException(status_code=404, detail=f"Your search for '{tag}' returned no results")
