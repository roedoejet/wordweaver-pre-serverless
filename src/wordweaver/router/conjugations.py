''' This is the API endpoint for Conjugations
'''
import os
from enum import Enum
from typing import List

from aiofiles import os as aos
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from wordweaver.data import CONJUGATION_DATA, DATA_PATH, WWLANG
from wordweaver.models import Response, Tier
from wordweaver.router.utils import CsvFile, DocxFile, FileSettings, LatexFile

router = APIRouter()

class ResponseType(str, Enum):
    csv = "csv"
    docx = 'docx'
    latex = 'latex'
    # pdf = 'pdf'

def create_files(conjugations,
                 file_type: ResponseType = Query('docx', alias="file-type"), tiers: List[Tier] = None,
                 settings: FileSettings = FileSettings()):
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

def filter_conjugations(root: List[str] = Query(None), option: List[str] = Query(None),
                                agent: List[str] = Query(None), patient: List[str] = Query(None)):
    filtered = CONJUGATION_DATA
    if root or agent or patient or option:
        for k, v in {'root': root, 'agent': agent, 'patient': patient, 'option': option}.items():
            if v:
                filtered = [x for x in filtered if x['input'][k] in v]
        return filtered

@router.get("/conjugations", response_model=Response, tags=["conjugations"])
def read_conjugations_from_file(root: List[str] = Query(None), option: List[str] = Query(None),
                                agent: List[str] = Query(None), patient: List[str] = Query(None)) -> Response:
    if root or agent or patient or option:
        return filter_conjugations(root=root, option=option, agent=agent, patient=patient)
    else:
        headers = {'Content-Encoding': 'gzip'}
        return FileResponse(path=os.path.join(DATA_PATH, WWLANG, 'conjugations.json.gz'), headers=headers)



@router.post("/files", tags=['conjugations'])
def create_files_from_file_request(root: List[str] = Query(None), option: List[str] = Query(None),
                                   agent: List[str] = Query(None), patient: List[str] = Query(None), file_type: ResponseType = Query('docx', alias="file-type"), tiers: List[Tier] = None,
                                   settings: FileSettings = FileSettings()):
    filtered = filter_conjugations(root=root, option=option, agent=agent, patient=patient)
    return create_files(conjugations=filtered, file_type=file_type, tiers=tiers, settings=settings)
