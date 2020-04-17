from fastapi import APIRouter
from typing import List
from wwapi.models import Tier

TIERS: List[Tier] = [
    # Display
    {"name": "ww.tiers.display",
     "separator": "",
     "order": 0,
     "key": "value"},
    # Breakdown
    {"name": "ww.tiers.breakdown",
     "separator": "-",
     "order": 1,
     "key": "value"},
    # Gloss
    {"name": "ww.tiers.gloss",
     "separator": "-",
     "order": 2,
     "key": "gloss"},
    # Breakdown Translation
    {"name": "ww.tiers.breakdown-translation",
     "separator": "-",
     "order": 3,
     "key": "english"},
    # Translation
    {"name": "ww.tiers.translation",
     "separator": "",
     "order": 4,
     "key": "english"},
]

router = APIRouter()

@router.get("/tiers", response_model=List[Tier])
def read_tiers() -> List[Tier]:
    return TIERS
