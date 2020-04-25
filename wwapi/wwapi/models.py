from __future__ import annotations
from pydantic import BaseModel
from typing import Any, List, Optional, Union
from enum import Enum


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

# Validation


class Condition(BaseModel):
    logic: Union[str, None]
    conditions: Optional[Any]
    method: Optional[str]
    method_key: Optional[str]
    item_key: Optional[str]
    value: Optional[Union[str, List[str]]]
    operator: Optional[str]


Conditions = Union[bool, List[Condition]]


class CategoryValidation(BaseModel):
    verbs: Conditions
    options: Conditions
    agents: Conditions
    patients: Conditions
    conjugations: Optional[Conditions]


class DisplayConditions(BaseModel):
    categories: CategoryValidation

class ValidationConditions(BaseModel):
    selection: CategoryValidation

class Validation(BaseModel):
    display: DisplayConditions
    validation: ValidationConditions


Response = List[ResponseObject]
