from typing import List, Optional, Union

from pydantic import BaseModel


class TranslationBase(BaseModel):
    en: Union[str, dict]
    fr: Union[str, dict]


class ModelConfig:
    use_enum_values = True


class Morpheme(BaseModel):
    value: str = ""
    position: int = 0


class Option(TranslationBase):
    """ Required """

    tag: str = ""
    type: str = ""


class Pronoun(TranslationBase):
    """ Required """

    person: str = ""
    number: str = ""
    gender: str = ""
    tag: str = ""


class Verb(TranslationBase):
    """ Required """

    tag: str = ""
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
