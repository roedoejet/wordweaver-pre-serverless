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
    gloss: str = ''
    tag: str = ''
    classes: List[str] = []


class Pronoun(BaseModel):
    ''' Required '''
    gloss: str = ''
    tag: str = ''


class Option(BaseModel):
    ''' Required '''
    gloss: str = ''
    tag: str = ''


class ConjugationInput(BaseModel):
    root: str
    option: str
    agent: str


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
