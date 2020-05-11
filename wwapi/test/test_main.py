import os
from unittest import TestCase, main
from unittest.mock import patch

from fastapi.testclient import TestClient

from wwapi.main import app

class MainTest(TestCase):
    """Main Tests for API
    """

    def setUp(self):
        self.client = TestClient(app)
        self.wwlangs = ['moh', 'fr']
        

    def test_read_main(self):
        for lang in self.wwlangs:
            with patch.dict('os.environ', {'WWLANG': lang}):
                self.assertIn('WWLANG', os.environ)
                for route in app.routes:
                    if not "{" in route.path:
                        print(route.path)
                        response = self.client.get(route.path)
                        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    main()