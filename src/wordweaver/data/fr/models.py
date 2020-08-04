from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel


class TranslationBase(BaseModel):
    en: Union[str, dict]
    fr: Union[str, dict]

class ModelConfig:
    use_enum_values = True

class Morpheme(BaseModel):
    value: str = ''
    position: int = 0


class TierOptions(BaseModel):
    language: str = 'L1'
    showName: bool = False

class TierValues(str, Enum):
    # Must be key in ResponseMorpheme
    gloss: "gloss"
    english: "english"
    value: "value"

class Tier(BaseModel):
    name: str = ''
    separator: str = ''
    position: int = 0
    key: str = 'value' # Must be key in ResponseMorpheme
    options: TierOptions = TierOptions()

    Config = ModelConfig


class Option(TranslationBase):
    ''' Required '''
    tag: str = ''
    type: str = ''


class Pronoun(TranslationBase):
    ''' Required '''
    person: str = ''
    number: str = ''
    gender: str = ''
    tag: str = ''


class Verb(TranslationBase):
    ''' Required '''
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
