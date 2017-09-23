import unittest

from app import app

class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        assert 'OK' in self.app.get('/').data