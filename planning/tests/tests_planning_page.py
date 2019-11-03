from django.test import TestCase, Client
from django.contrib.auth import login, authenticate
from planning.views import planning, planning_pm
from planning.models import PlanningAm, PlanningPm
from fooddish.models import Fooddish
from usercontrol.models import User


# Create your tests here.
class PlanningPageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        self.user = User.objects.create_user(
            'userTest',
            'testuser@test.com',
            'PwdUserTest',
            number=670217836
        )
        self.days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        self.allUser = User.objects.all()

    def test_status_code_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.status_code, 200)

    def test_template_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertTemplateUsed('planning/index.html')

    def test_view_page_planning(self):
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.resolver_match.func, planning)

    def test_context_page_planning(self):
        self.cli.login(username=self.user.username, password='PwdUserTest')
        rep = self.cli.get('/planning/')
        self.assertEqual(rep.context['days'], self.days)
        self.assertEqual(len(rep.context['users']), len(self.allUser))
        self.assertEqual(rep.context['users'][0].id, self.allUser[0].id)
        self.assertEqual(rep.context['dishs'], {})
        self.assertEqual(len(rep.context['planning']), len(PlanningAm.objects.all()))

    def test_context_page_planning_pm(self):
        self.cli.login(username=self.user.username, password='PwdUserTest')
        rep = self.cli.get('/planning/pm')
        self.assertEqual(rep.context['days'], self.days)
        self.assertEqual(len(rep.context['users']), len(self.allUser))
        self.assertEqual(rep.context['users'][0].id, self.allUser[0].id)
        self.assertEqual(rep.context['dishs'], {})
        self.assertEqual(len(rep.context['planning']), len(PlanningPm.objects.all()))

    def test_status_code_page_planning_pm(self):
        rep = self.cli.get('/planning/pm')
        self.assertEqual(rep.status_code, 200)

    def test_template_page_planning_pm(self):
        rep = self.cli.get('/planning/pm')
        self.assertTemplateUsed('planning/pm.html')

    def test_view_page_planning_pm(self):
        rep = self.cli.get('/planning/pm')
        self.assertEqual(rep.resolver_match.func, planning_pm)

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        self.user = User.objects.create_user(
            'userTest',
            'testuser@test.com',
            'PwdUserTest',
            number=670217836
        )
        self.user2 = User.objects.create_user(
            'userTestNumberTwo',
            'testusertwo@test.com',
            'PwdUserTest',
            number=670217836
        )
        planning = PlanningAm()
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
        planning2 = PlanningPm()
        planning2.monday = "Plat 1"
        planning2.tuesday = "Plat 2"
        planning2.wednesday = "Plat 3"
        planning2.thursday = "Plat 4"
        planning2.friday = "Plat 5"
        planning2.saturday = "Plat 6"
        planning2.sunday = "Plat 7"
        planning2.moment_day = "am"
        planning2.id_user = self.user
        planning2.save()
        foo = Fooddish()
        foo.name = "Tacos"
        foo.save()
        foo2 = Fooddish()
        foo2.name = "Burger"
        foo2.save()
        self.plann = planning
        self.plann2 = planning2
        self.food = foo
        self.food2 = foo2

    def test_create_new_planning(self):
        data1 = {
            'days1': 'Plat 1',
            'days2': 'Plat 2',
            'days3': 'Plat 3',
            'days4': 'Plat 4',
            'days5': 'Plat 5',
            'days6': 'Plat 6',
            'days7': 'Plat 7',
            'momentDay' : 'am'
            }
        data2 = {
            'days1': 'Plat 1',
            'days2': 'Plat 2',
            'days3': 'Plat 3',
            'days4': 'Plat 4',
            'days5': 'Plat 5',
            'days6': 'Plat 6',
            'days7': 'Plat 7',
            'momentDay' : 'pm'
            }
        self.cli.login(username=self.user2.username, password='PwdUserTest')
        rep1 = self.cli.post('/planning/set', data1)
        self.assertTrue(rep1.json()['ServeurResponse'])
        rep2 = self.cli.post('/planning/set', data2)
        self.assertTrue(rep2.json()['ServeurResponse'])

    def test_remove_planning_am(self):
        data = {'id_planning': self.plann.pk, 'momentDay': 'am'}
        rep = self.cli.post('/planning/remove', data)
        self.assertTrue(rep.json()['ServeurResponse'])

    def test_fail_remove_planning(self):
        rep = self.cli.get('/planning/remove')
        self.assertFalse(rep.json()['ServeurResponse'])

    def test_update_planning_am(self):
        data = {
            'id': self.plann.id,
            'monday': self.food.id,
            'tuesday': self.food.id,
            'wednesday': self.food.id,
            'thursday': self.food2.id,
            'friday': self.food2.id,
            'saturday': self.food.id,
            'sunday': self.food2.id,
            'momentDay': 'am'
        }

        rep = self.cli.post('/planning/update', data)
        self.assertTrue(rep.json()['ServeurResponse'])

        check = PlanningAm.objects.get(id=self.plann.pk).monday
        self.assertEqual(check, self.food.name)

    def test_remove_planning_pm(self):
        data = {'id_planning': self.plann2.pk, 'momentDay': 'pm'}
        rep = self.cli.post('/planning/remove', data)
        self.assertTrue(rep.json()['ServeurResponse'])

    def test_update_planning_pm(self):
        data = {
            'id': self.plann2.id,
            'monday': self.food.id,
            'tuesday': self.food.id,
            'wednesday': self.food.id,
            'thursday': self.food2.id,
            'friday': self.food2.id,
            'saturday': self.food.id,
            'sunday': self.food2.id,
            'momentDay': 'pm'
        }

        rep = self.cli.post('/planning/update', data)
        self.assertTrue(rep.json()['ServeurResponse'])

        check = PlanningPm.objects.get(id=self.plann2.pk).monday
        self.assertEqual(check, self.food.name)

    def test_duplicate_planning_database_error_for_user(self):
        data = {
            'days1': 'Plat 1',
            'days2': 'Plat 2',
            'days3': 'Plat 3',
            'days4': 'Plat 4',
            'days5': 'Plat 5',
            'days6': 'Plat 6',
            'days7': 'Plat 7',
            'momentDay': 'am'
            }
        self.cli.login(username=self.user.username, password='PwdUserTest')
        rep = self.cli.post('/planning/set', data)
        self.assertFalse(rep.json()['ServeurResponse'])
        self.assertTrue(rep.json()['error'])