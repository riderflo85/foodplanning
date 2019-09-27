from django.test import TestCase, Client
from planning.views import planning
from planning.models import Planning
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
        planning = Planning()
        planning.monday = "Plat 1"
        planning.tuesday = "Plat 2"
        planning.wednesday = "Plat 3"
        planning.thursday = "Plat 4"
        planning.friday = "Plat 5"
        planning.saturday = "Plat 6"
        planning.sunday = "Plat 7"
        planning.moment_day = "am"
        planning.id_user = self.user
        planning.save()
        self.plann = planning

    def test_create_new_planning(self):
        data = {
            'days1': 'Plat 1',
            'days2': 'Plat 2',
            'days3': 'Plat 3',
            'days4': 'Plat 4',
            'days5': 'Plat 5',
            'days6': 'Plat 6',
            'days7': 'Plat 7'
            }
        self.cli.login(username=self.user.username, password='PwdUserTest')
        rep = self.cli.post('/planning/set', data)
        self.assertTrue(rep.json()['ServeurResponse'])

    def test_remove_planning(self):
        data = {'id_planning': self.plann.pk}
        rep = self.cli.post('/planning/remove', data)
        self.assertTrue(rep.json()['ServeurResponse'])

    def test_fail_remove_planning(self):
        rep = self.cli.get('/planning/remove')
        self.assertFalse(rep.json()['ServeurResponse'])