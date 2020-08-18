from pydantic import BaseModel
from typing import Any, List, Optional, Union
from enum import Enum

class TranslationBase(BaseModel):
    en: Union[str, dict]
    moh: Union[str, dict]

class Morpheme(BaseModel):
    value: str = ''
    position: int = 0

class TierOptions(BaseModel):
    language: str = 'L1'
    showName: bool = False


class Tier(BaseModel):
    name: str = ''
    separator: str = ''
    position: int = 0
    key: str = ''           # Must be key in ResponseMorpheme
    options: TierOptions

class Verb(BaseModel):
    ''' Required '''
    tag: str = ''
    classes: List[str] = []


class Pronoun(BaseModel):
    ''' Required '''
    tag: str = ''


class Option(BaseModel):
    ''' Required '''
    tag: str = ''
    type: str = ''


class ConjugationInput(BaseModel):
    root: str
    option: str
    subject: str


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
