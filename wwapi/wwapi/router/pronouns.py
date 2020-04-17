''' This is the API endpoint for Pronouns
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Pronoun
# Data
from wwapi.data import PRONOUN_DATA

router = APIRouter()

@router.get("/pronouns", response_model=List[Pronoun])
def read_pronouns() -> List[Pronoun]:
    pronouns = PRONOUN_DATA
    return pronouns
