import json
import requests

from docx import Document
from typing import List
from pydantic import BaseModel

from wwapi.data import URL
from wwapi.models import Response, Tier

class FileSettings(BaseModel):
    heading: str = 'Conjugations'

class File:
    """[summary]
    """

    def __init__(self, conjugations: Response = None, tiers: List[Tier] = None):
        self._conjugations = conjugations
        self._tiers = tiers
        self.format()

    @property
    def conjugations(self):
        """
        """
        return self._conjugations

    @property
    def tiers(self):
        """
        """
        return self._tiers

    @property
    def formatted_data(self):
        """[summary]
        """
        return self._formatted_data

    def format(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self._formatted_data = []
        for conjugation in self.conjugations:
            tiered_conjugation = []
            for tier in self.tiers:
                tier = tier.dict()
                # Filter empty and sort by position
                output = sorted([x for x in conjugation['output']
                        if x[tier['key']]], key=lambda x: x['position'])
                # Join with separator
                output = tier['separator'].join(map(lambda x: x[tier['key']], output))
                tiered_conjugation.append({'name': tier['name'],
                                           'options': tier['options'],
                                           'output': output})
            self._formatted_data.append(tiered_conjugation)


class DocxFile(File):
    def __init__(self, conjugations, tiers, settings: FileSettings):
        self.document = Document()
        super(DocxFile, self).__init__(conjugations, tiers)
        self.settings = settings.dict()

    def export(self):
        # Add header
        self.document.add_heading(self.settings['heading'], 0)
        # Add each tier
        for conjugation in self.formatted_data:
            tiers = '\n'.join(map(lambda x: x['output'], conjugation))
            self.document.add_paragraph(tiers, style="List Number")
            self.document.add_paragraph()
        return self.document


class LatexFile(File):
    def __init__(self, conjugations, tiers, **kwargs):
        super(LatexFile, self).__init__(conjugations, tiers)
        self.kwargs = kwargs

    def export(self):
        return

class CsvFile(File):
    def __init__(self, conjugations, tiers, **kwargs):
        super(CsvFile, self).__init__(conjugations, tiers)
        self.kwargs = kwargs


def find(db_name, selector):
    # This needs to be updated in the router
    headers = {'Content-type': 'application/json'}
    url = f'{URL}/{db_name}/_find'
    response = requests.post(url, data=json.dumps(
        {'selector': selector}), headers=headers)
    return response.json()
