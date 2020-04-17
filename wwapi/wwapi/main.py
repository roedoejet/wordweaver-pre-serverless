"""Main WordWeaver run file
"""

from fastapi import FastAPI

from wwapi.router import affixes, pronouns, tiers, verbs

# FastAPI specific code
app = FastAPI()

app.include_router(
    affixes.router,
    prefix='/api/v1'
)

app.include_router(
    pronouns.router,
    prefix='/api/v1'
)

app.include_router(
    tiers.router,
    prefix='/api/v1'
)

app.include_router(
    verbs.router,
    prefix='/api/v1'
)