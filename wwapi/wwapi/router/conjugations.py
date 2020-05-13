''' This is the API endpoint for Conjugations
'''
import os
from aiofiles import os as aos
from tempfile import mkstemp
from typing import List
from enum import Enum

from fastapi import APIRouter, Query, Response as FAResponse
from fastapi.responses import FileResponse

from wwapi.router.utils import CsvFile, DocxFile, LatexFile, find, FileSettings
from wwapi.models import Response, Tier

router = APIRouter()

DB_NAME = 'data'


class ResponseType(str, Enum):
    csv = "csv"
    docx = 'docx'
    latex = 'latex'
    # pdf = 'pdf'


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


@router.post("/files", tags=['conjugations'])
def create_files(root: List[str] = Query(None), option: List[str] = Query(None),
                 agent: List[str] = Query(None), patient: List[str] = Query(None),
                 file_type: ResponseType = Query('docx', alias="file-type"), tiers: List[Tier] = None,
                 settings: FileSettings = FileSettings()):
    conjugations = read_conjugations(root, option, agent, patient)
    if file_type == 'docx':   
        document = DocxFile(conjugations, tiers, settings)
        path = document.write_to_temp()
        media_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        fn = "conjugations.docx"

    if file_type == 'csv':
        document = CsvFile(conjugations, tiers, settings)
        path = document.write_to_temp()
        media_type = "text/csv"
        fn = "conjugations.csv"

    if file_type == 'latex':
        document = LatexFile(conjugations, tiers, settings)
        path = document.write_to_temp()
        media_type = "text/plain"
        fn = "conjugations.tex"

    # TODO: LaTeX is not creating a PDF properly and causing lots of errors 
    # if file_type == 'pdf':
    #     document = LatexFile(conjugations, tiers, settings)
    #     path = document.write_to_temp(ftype='pdf')
    #     media_type = "application/pdf"
    #     fn = "conjugations.pdf"

    try:
        headers = {'Content-Disposition': f'attachment; filename="{fn}"'}
        response = FileResponse(path=path,
                                filename=fn,
                                media_type=media_type, headers=headers)
        return response
    finally:
        aos.remove(path)
