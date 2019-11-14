from django.test import TestCase
from django.utils.safestring import mark_safe
from usercontrol.models import User, SecretKeySave
from planning.forms import SeeAnotherPlanningForm
from planning.functions import check_user_planning_am, check_user_planning_pm, all_key_save

from planning.models import PlanningAm, PlanningPm


class CheckUserPlanningTestCase(TestCase):
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


class SecretKeySavedTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'userTest',
            'testuser@test.com',
            'PwdUserTest',
            number=670217836,
            secret_key="abfjEGTLpou3!:;^é'-REDF4"
        )
        self.user2 = User.objects.create_user(
            'userTest2',
            'testuser2@test.com',
            'PwdUser2Test',
            number=673517836,
            secret_key="abfjE123pou3!:;^é'-REDF4"
        )
        self.user3 = User.objects.create_user(
            'userTest3',
            'testuser3@test.com',
            'PwdUser3Test',
            number=670211136,
            secret_key="bf456TLpou3mùoe$^é'-REDF4"
        )
        self.key_save1 = SecretKeySave(
            secret_key_saved=self.user2.secret_key,
            users=self.user1
        ).save()
        self.key_save2 = SecretKeySave(
            secret_key_saved=self.user3.secret_key,
            users=self.user1
        ).save()

    def test_listing_key_save(self):
        data = [
            {
                'secret_key_saved': "abfjE123pou3!:;^é'-REDF4",
                'username': 'userTest2'
            },
            {
                'secret_key_saved': "bf456TLpou3mùoe$^é'-REDF4",
                'username': 'userTest3'
            }
        ]
        result = all_key_save(self.user1)
        self.assertEqual(result, data)

    def test_listing_key_save_error(self):
        data = [('Error', 'Erreur')]
        result = all_key_save('error_user')
        self.assertEqual(result, data)

    def test_listing_key_save_not_match(self):
        data = []
        result = all_key_save(self.user3)
        self.assertEqual(result, data)

    def test_list_key_saved_with_form(self):
        form = SeeAnotherPlanningForm(req_user=self.user1)
        print(form['secret_key'])
        print(form['key_save'])