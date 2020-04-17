from fastapi import APIRouter
from typing import List
from wwapi.models import Tier

from wwapi.data.utils import find

router = APIRouter()


@router.get("/tiers", response_model=List[Tier], tags=["tiers"])
def read_tiers() -> List[Tier]:
    tiers = find({'data_type': 'tier'}) 
    return tiers['docs']
