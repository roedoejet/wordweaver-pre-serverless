''' This is the API endpoint for Conjugations
'''
import os
from aiofiles import os as aos
from tempfile import mkstemp
from typing import List
from enum import Enum

from fastapi import APIRouter, Query, Response as FAResponse
from fastapi.responses import FileResponse

from wwapi.router.utils import DocxFile, find, FileSettings
from wwapi.models import Response, Tier

router = APIRouter()

DB_NAME = 'data'


class ResponseType(str, Enum):
    csv = "csv"
    docx = 'docx'
    latex = 'latex'


def return_selector(arg):
    if not arg:
        return False
    if len(arg) == 1:
        return arg[0]
    else:
        return {"$in": arg}


@router.get("/conjugations", response_model=Response, tags=["conjugations"])
def read_conjugations(root: List[str] = Query(None), option: List[str] = Query(None),
                      agent: List[str] = Query(None), patient: List[str] = Query(None)) -> Response:
    selector = {}
    agent = return_selector(agent)
    patient = return_selector(patient)
    option = return_selector(option)
    conjugations = []
    # Queries have to be joined because for some un-relaxing reason,
    # CouchDB queries with $in or $or do not actually use indices
    if root:
        for root_tag in root:
            selector['input.root'] = root_tag
            if option:
                selector['input.option'] = option
            if agent:
                selector['input.agent'] = agent
            if patient:
                selector['input.patient'] = patient
            conjugations += find(DB_NAME, selector)['docs']
    return conjugations


@router.post("/conjugations", tags=['conjugations'])
def create_files(root: List[str] = Query(None), option: List[str] = Query(None),
                 agent: List[str] = Query(None), patient: List[str] = Query(None),
                 file_type: ResponseType = 'docx', tiers: List[Tier] = None,
                 settings: FileSettings = FileSettings()):
    conjugations = read_conjugations(root, option, agent, patient)

    if file_type == 'docx':
        df = DocxFile(conjugations, tiers, settings)
        document = df.export()
        fd, path = mkstemp()
        document.save(path)
        try:
            response = FileResponse(path=path,
                                    filename="conjugations.docx",
                                    media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            return response
        finally:
            aos.remove(path)

    if file_type == 'csv':
        pass

    if file_type == 'latex':
        pass