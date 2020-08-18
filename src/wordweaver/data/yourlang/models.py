from typing import List, Optional, Union

from pydantic import BaseModel


class TranslationBase(BaseModel):
    en: Union[str, dict]


class Morpheme(BaseModel):
    value: str = ""
    position: int = 0


class Verb(BaseModel):
    """ Required """

    tag: str = ""
    classes: List[str] = []


class Pronoun(BaseModel):
    """ Required """

    tag: str = ""


class Option(BaseModel):
    """ Required """

    tag: str = ""
    type: str = ""


class ConjugationInput(BaseModel):
    root: str
    option: str
    agent: str


class ResponseMorpheme(BaseModel):
    position: Optional[int]
    value: Optional[str]
    gloss: Optional[str]


Conjugation = List[ResponseMorpheme]


class ResponseObject(BaseModel):
    input: ConjugationInput
    output: Conjugation


Response = List[ResponseObject]
