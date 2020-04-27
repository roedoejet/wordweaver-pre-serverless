"""Main WordWeaver run file
"""

from fastapi import FastAPI

from wwapi.router import conjugations, options, pronouns, verbs

# FastAPI specific code
app = FastAPI()

app.include_router(
    options.router,
    prefix='/api/v1'
)

app.include_router(
    pronouns.router,
    prefix='/api/v1'
)

app.include_router(
    verbs.router,
    prefix='/api/v1'
)

app.include_router(
    conjugations.router,
    prefix='/api/v1'
)
