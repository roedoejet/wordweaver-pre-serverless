from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class AffixType(Enum):
    aspect = 1
    required = 2
    temporal = 3
    post_aspect = 4


class Morpheme(BaseModel):
    value: str = ''
    position: int = 0


class Affix(BaseModel):
    tag: str = ''
    gloss: str = ''
    type: str = ''
    morphemes: List[Morpheme]


class TierOptions(BaseModel):
    language: str = 'L1'
    showName: bool = False


class Tier(BaseModel):
    name: str = ''
    separator: str = ''
    position: int = 0
    key: str = ''           # Must be key in ResponseMorpheme
    options: Optional[TierOptions]


class AffixOption(BaseModel):
    ''' Required '''
    tag: str = ''
    gloss: str = ''
    affixes: List[Affix]


class Pronoun(BaseModel):
    ''' Required '''
    person: str = ''
    number: str = ''
    gender: str = ''
    inclusivity: str = ''
    role: str = ''
    value: str = ''
    gloss: str = ''
    obj_gloss: str = ''
    position: int = 0
    tag: str = ''


class Verb(BaseModel):
    ''' Required '''
    thematic_relation: str = ''
    display: str = ''
    gloss: str = ''
    tag: str = ''
    required_affixes: List[Affix]
    position: int = 0


class ConjugationInput(BaseModel):
    root: str
    affopt: str
    agent: str
    patient: str


class OptionalParam(BaseModel):
    param: str
    value: str


class RequestParams(BaseModel):
    root: List[str]
    affopt: List[str]
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