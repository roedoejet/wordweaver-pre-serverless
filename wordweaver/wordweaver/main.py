"""Main WordWeaver run file
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from wordweaver.router import conjugations, options, pronouns, verbs

# FastAPI specific code
app = FastAPI(title="WordWeaver API",
    description="Welcome to the WordWeaver documentation. Please visit <a href='https://docs.wordweaver.ca'>https://docs.wordweaver.ca</a> for more information.",
    version="1.0",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
    