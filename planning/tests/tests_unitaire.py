from django.test import TestCase
from django.utils.safestring import mark_safe
from usercontrol.models import User
from planning.functions import check_user_planning_am
from planning.models import PlanningAm


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
        self.plann = planning

    def test_check_user_planning_function(self):
        rep = check_user_planning_am(self.user)
        self.assertEqual(rep[0], self.plann)

    def test_check_user_planning_function_fail(self):
        rep = check_user_planning_am('not_user')
        self.assertFalse(rep)
