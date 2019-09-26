from django.test import TestCase, Client
from planning.views import planning


# Create your tests here.
class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.status_code, 200)