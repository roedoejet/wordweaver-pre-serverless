from unittest import TestCase

from fastapi.testclient import TestClient

from wwapi.main import app

class BuildTest(TestCase):
    """Tests for constructing file format exports
    """

    def setUp(self):
        self.client = TestClient(app)
        self.wwlangs = ['moh', 'fr']