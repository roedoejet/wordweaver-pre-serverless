''' This is the API endpoint for Verbs
'''

from typing import List

from fastapi import APIRouter

from wwapi.models import Verb
# Data
from wwapi.data import VERB_DATA

router = APIRouter()

@router.get("/verbs", response_model=List[Verb])
def read_verbs() -> List[Verb]:
    verbs = VERB_DATA
    return verbs

# # API Route
# @router.get("/verbs", response_model=List[Verb])
# def read_verbs(verb_filter: Verb = {}) -> List[Verb]:
#     bucket = get_bucket()
#     verbs = get_verbs(bucket, verb_filter)
#     return verbs

# # DB Handler
# def get_verbs(bucket: Bucket, verb_filter: Verb):
#     doc_id = f"verbs"
#     result = bucket.get(doc_id, quiet=True)
#     if not result.value:
#         return None
#     print(result.value)
#     return result.value
