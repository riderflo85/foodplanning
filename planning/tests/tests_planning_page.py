from django.test import TestCase, Client
from planning.views import planning
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


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

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        self.user = User.objects.create_user('userTest', 'testuser@test.com', 'PwdUserTest')

    def test_create_new_planning(self):
        # rep = self.cli.post()
        pass