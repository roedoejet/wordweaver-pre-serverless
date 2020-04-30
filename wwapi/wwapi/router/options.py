''' This is the API endpoint for everything else
'''

from typing import List

from fastapi import APIRouter, Response, status, HTTPException

from wwapi.models import Option

from wwapi.router.utils import find

router = APIRouter()

DB_NAME = 'option'


@router.get("/options", response_model=List[Option], tags=["options"])
def read_options() -> List[Option]:
    selector = {
        "tag": {
            "$gt": 0
        }
    }
    options = find(DB_NAME, selector)['docs']
    return options


@router.get("/options/{tag}", response_model=Option, tags=["options"])
def read_option_by_id(tag: str, response: Response) -> Option:
    selector = {
        "tag": tag
    }
    options = find(DB_NAME, selector)['docs']
    if len(options) > 1:
        response.status_code = status.HTTP_206_PARTIAL_CONTENT
    if len(options) < 1:
        raise HTTPException(
            status_code=404, detail="Your search returned no results")
    return options[0]
