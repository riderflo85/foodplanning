from django.test import TestCase
from django.utils.safestring import mark_safe
from usercontrol.models import User
from planning.functions import check_user_planning_am, check_user_planning_pm
from planning.models import PlanningAm, PlanningPm


class UnitaireTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'userTest',
            'testuser@test.com',
            'PwdUserTest',
            number=670217836
        )
        self.user.first_name = 'test_first_name'
        self.user.save()
        planning_am = PlanningAm()
        planning_am.monday = "Plat 1"
        planning_am.tuesday = "Plat 2"
        planning_am.wednesday = "Plat 3"
        planning_am.thursday = "Plat 4"
        planning_am.friday = "Plat 5"
        planning_am.saturday = "Plat 6"
        planning_am.sunday = "Plat 7"
        planning_am.moment_day = "am"
        planning_am.id_user = self.user
        planning_am.save()
        planning_pm = PlanningPm()
        planning_pm.monday = "Plat 1"
        planning_pm.tuesday = "Plat 2"
        planning_pm.wednesday = "Plat 3"
        planning_pm.thursday = "Plat 4"
        planning_pm.friday = "Plat 5"
        planning_pm.saturday = "Plat 6"
        planning_pm.sunday = "Plat 7"
        planning_pm.moment_day = "pm"
        planning_pm.id_user = self.user
        planning_pm.save()
        self.plann_am = planning_am
        self.plann_pm = planning_pm

    def test_check_user_planning_am_function(self):
        rep = check_user_planning_am(self.user)
        self.assertEqual(rep[0], self.plann_am)

    def test_check_user_planning_am_function_fail(self):
        rep = check_user_planning_am('not_user')
        self.assertFalse(rep)

    def test_check_user_planning_pm_function(self):
        rep = check_user_planning_pm(self.user)
        self.assertEqual(rep[0], self.plann_pm)

    def test_check_user_planning_pm_function_fail(self):
        rep = check_user_planning_pm('not_user')
        self.assertFalse(rep)