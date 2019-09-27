from django.test import TestCase, Client
from planning.views import planning


# Create your tests here.
class PlanningPageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_status_code_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.status_code, 200)

    def test_template_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertTemplateUsed('planning/index.html')

    def test_view_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.resolver_match.func, planning)