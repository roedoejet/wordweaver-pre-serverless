from __future__ import annotations
from pydantic import BaseModel
from typing import Any, List, Optional, Union
from enum import Enum


class Morpheme(BaseModel):
    value: str = ''
    position: int = 0


class Option(BaseModel):
    ''' Required '''
    gloss: str = ''
    tag: str = ''


class Pronoun(BaseModel):
    ''' Required '''
    person: str = ''
    number: str = ''
    gender: str = ''
    inclusivity: str = ''
    role: str = ''
    gloss: str = ''
    obj_gloss: str = ''
    position: int = 0
    tag: str = ''


class Verb(BaseModel):
    ''' Required '''
    gloss: str = ''
    tag: str = ''
    classes: List[str] = []


class ConjugationInput(BaseModel):
    root: str
    option: str
    agent: Union[List[str], str]


class OptionalParam(BaseModel):
    param: str
    value: str


class RequestParams(BaseModel):
    root: List[str]
    option: List[str]
    agent: List[str]
    patient: List[str]
    optional: Optional[List[OptionalParam]]


class ResponseMorpheme(BaseModel):
    position: Optional[int]
    value: Optional[str]
    gloss: Optional[str]
    english: Optional[str]
    type: Optional[List[str]]


Conjugation = List[ResponseMorpheme]


class ResponseObject(BaseModel):
    input: ConjugationInput
    output: Conjugation


Response = List[ResponseObject]
