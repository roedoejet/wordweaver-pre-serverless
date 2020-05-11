"""Main WordWeaver run file
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from wwapi.router import conjugations, options, pronouns, verbs

# FastAPI specific code
app = FastAPI()

@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse("/docs")

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
    