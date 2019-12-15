from django.test import TestCase, Client
from api.views import get_dish
from usercontrol.models import User
from planning.models import PlanningAm, PlanningPm


class EndpointApiTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user = User.objects.create_user(
            'testusername',
            'test@test.com',
            'passwordforusertest',
            number=71254869
        )
        plann_am = PlanningAm()
        plann_am.monday = "Magret de canard"
        plann_am.tuesday = "Couscous"
        plann_am.wednesday = "Raclette"
        plann_am.thursday = "Steak-frites"
        plann_am.friday = "Petits légumes farcis"
        plann_am.saturday = "Pot au feu maison"
        plann_am.sunday = "Croc monsieur"
        plann_am.id_user = user
        plann_am.save()
        plann_pm = PlanningPm()
        plann_pm.monday = "Ratatouille"
        plann_pm.tuesday = "Spaghetti à la bolognaise"
        plann_pm.wednesday = "Panini"
        plann_pm.thursday = "Gratin de courgette"
        plann_pm.friday = "Pate lardon"
        plann_pm.saturday = "Côte de bœuf"
        plann_pm.sunday = "Tacos"
        plann_pm.id_user = user
        plann_pm.save()
        self.user = user
        self.planning_am = plann_am
        self.planning_pm = plann_pm

    def test_view_get_dish_am(self):
        data = {
            "username": self.user.username,
            "day": "monday",
            "amOrPm": "am"
        }
        rep = self.cli.post('/api/v1/dish', data)
        self.assertEqual(rep.status_code, 200)
        self.assertEqual(rep.resolver_match.func, get_dish)
        self.assertEqual(rep.json()['dish'], self.planning_am.monday)

    def test_view_get_dish_pm(self):
        data = {
            "username": self.user.username,
            "day": "monday",
            "amOrPm": "pm"
        }
        rep = self.cli.post('/api/v1/dish', data)
        self.assertEqual(rep.status_code, 200)
        self.assertEqual(rep.resolver_match.func, get_dish)
        self.assertEqual(rep.json()['dish'], self.planning_pm.monday)

    def test_view_get_dish_am_fail(self):
        data = {
            "username": 'user_does_not_exist',
            "day": "monday",
            "amOrPm": "am"
        }
        rep = self.cli.post('/api/v1/dish', data)
        self.assertEqual(rep.status_code, 200)
        self.assertEqual(rep.resolver_match.func, get_dish)
        self.assertTrue(rep.json()['error'])

    def test_view_get_dish_pm_fail(self):
        data = {
            "username": 'user_does_not_exist',
            "day": "monday",
            "amOrPm": "pm"
        }
        rep = self.cli.post('/api/v1/dish', data)
        self.assertEqual(rep.status_code, 200)
        self.assertEqual(rep.resolver_match.func, get_dish)
        self.assertTrue(rep.json()['error'])
