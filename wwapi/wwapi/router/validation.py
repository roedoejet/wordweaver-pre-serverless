''' This is the API endpoint for validation
'''
from fastapi import APIRouter

from wwapi.models import Validation

from wwapi.data import VALIDATION_DATA

from wwapi.data.utils import find

router = APIRouter()


@router.get("/validation", response_model=Validation, tags=["validation"])
def read_validation() -> Validation:
    validation = find({'data_type': 'validation'})
    print(validation)
    return validation['docs'][0]