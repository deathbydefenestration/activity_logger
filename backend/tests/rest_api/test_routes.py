from unittest import TestCase

from src import create_app


class TestAPI(TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def test_api_response_is_ok(self):
        response = self.client().post('/api/hello')
        value = response.json.get('hello')

        self.assertEqual(response.status_code, 200)
        self.assertEqual('me', value)
