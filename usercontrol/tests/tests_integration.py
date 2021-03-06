from django.test import TestCase, Client
from django.contrib.auth.models import Group, Permission
from usercontrol.forms import SignupForm, LoginForm
from usercontrol.views import sign_in, sign_up, sign_out, account,\
    edit_user_infos, change_passwd, manage_sms, remove_account
from usercontrol.models import User


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_sign_in(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_sign_up(self):
        rep = self.cli.get('/sign_up/')
        self.assertEqual(rep.status_code, 200)

    def test_page_sing_out(self):
        rep = self.cli.get('/sign_out/')
        self.assertEqual(rep.status_code, 302)

    def test_page_account(self):
        rep = self.cli.get('/account/')
        self.assertEqual(rep.status_code, 302)


class UserAuthenticateTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            email='testuser@founisseur.com',
            password='longpasswordtest',
            number=612345678
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.user = user_test

    def test_user_account_not_exist(self):
        data_no_user = {'user': 'failUser', 'password': 'notpassword'}
        rep = self.cli.post('/', data_no_user)
        self.assertTrue(rep.context['error'])
        # User is not redirect because authentification is failed
        self.assertEqual(rep.status_code, 200)

    def test_user_redirect_after_sign_in(self):
        data_for_login = {'user': 'testUser', 'password': 'longpasswordtest'}
        rep = self.cli.post('/', data_for_login)
        self.assertEqual(rep.status_code, 302)

    def test_user_sign_out(self):
        self.cli.login(
            username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/sign_out/')
        self.assertEqual(rep.status_code, 302)

    def test_create_new_user(self):
        data = {
            'pseudo': 'NewUser',
            'last_name': 'NEW',
            'first_name': 'UserFrech',
            'email': 'newuserfrech@frech.com',
            'password': 'thislongpasswordforlogin',
            'confirm_pwd': 'thislongpasswordforlogin',
            'phone_number': 670217836,
            'group_name': 'groupeTest'
        }
        rep = self.cli.post('/sign_up/', data)
        self.assertRedirects(rep, '/')

    def test_fail_create_new_user(self):
        data = {
            'pseudo': 'NewUser',
            'last_name': 'NEW',
            'first_name': 'UserFrech',
            'email': 'newuserfrechFAIL',
            'password': 'thislongpasswordforlogin',
            'confirm_pwd': 'thislongpasswordforlogin',
            'phone_number': 670217836,
            'group_name': 'groupeTest'
        }
        rep = self.cli.post('/sign_up/', data)
        self.assertFormError(
            rep,
            'form',
            'email',
            'Saisissez une adresse de courriel valide.'
        )


class FormTestCase(TestCase):
    def test_form_sign_up(self):
        form_data = {
            'pseudo': 'testUser',
            'last_name': 'FooTest',
            'first_name': 'Tester',
            'email': 'testuser@founisseur.com',
            'password': 'longpasswordtest',
            'confirm_pwd': 'longpasswordtest',
            'phone_number': 770207030,
            'group_name': 'groupeTest'
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_sign_in(self):
        form_data = {
            'user': 'testUser',
            'password': 'longpasswordtest',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())


class ViewsUsedTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_views_page_sing_in(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.resolver_match.func, sign_in)

    def test_views_page_sing_up(self):
        rep = self.cli.get('/sign_up/')
        self.assertEqual(rep.resolver_match.func, sign_up)

    def test_views_page_sing_out(self):
        rep = self.cli.get('/sign_out/')
        self.assertEqual(rep.resolver_match.func, sign_out)

    def test_views_page_account(self):
        rep = self.cli.get('/account/')
        self.assertEqual(rep.resolver_match.func, account)


class TemplateRenderTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            email='testuser@founisseur.com',
            password='test',
            number=612345678
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.cli.login(username=user_test.username, password='test')

    def test_template_page_sign_in(self):
        rep = self.cli.get('/')
        self.assertTemplateUsed(rep, 'usercontrol/sign_in.html')

    def test_template_page_sign_up(self):
        rep = self.cli.get('/sign_up/')
        self.assertTemplateUsed(rep, 'usercontrol/sign_up.html')

    def test_redirect_page_sign_out(self):
        rep = self.cli.get('/sign_out/')
        self.assertRedirects(rep, '/')

    def test_template_page_account(self):
        rep = self.cli.get('/account/')
        self.assertTemplateUsed(rep, 'usercontrol/account.html')


class ManageUserAccountTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            email='testuser@founisseur.com',
            password='testpassword',
            number=612345678
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.data = {
            'last_name': 'lastNameTest',
            'first_name': 'firstNameTest',
            'username': 'pseudoForTest',
            'email': 'emailtest@test.com',
            'number': 271235678,
            'group_name': 'groupeTest'
        }
        self.user = user_test

    def test_change_user_infos(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/edit_infos/', self.data)
        self.assertEqual(rep.resolver_match.func, edit_user_infos)
        self.assertTrue(rep.json()['success'])
        self.assertEqual(rep.status_code, 200)

    def test_permission_denied_change_user_infos(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.get('/edit_infos/')
        self.assertFalse(rep.json()['success'])

    def test_change_user_fail(self):
        rep = self.cli.get('/edit_infos/')
        self.assertEqual(rep.status_code, 302)
        self.assertRedirects(rep, '/')

    def test_change_user_password(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/change_pwd/', {'new_pwd': 'newPasswordForTest'})
        self.assertTrue(rep.json()['success'])
        self.assertEqual(rep.resolver_match.func, change_passwd)

    def test_permission_denied_change_user_password(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.get('/change_pwd/')
        self.assertFalse(rep.json()['success'])

    def test_change_user_password_fail(self):
        rep = self.cli.get('/change_pwd/')
        self.assertEqual(rep.status_code, 302)
        self.assertRedirects(rep, '/')

    def test_active_notifiaction_sms(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/manage_sms/', {'active': 'true'})
        self.assertEqual(rep.status_code, 200)
        self.assertTrue(rep.json()['actived'])
        self.assertTrue(User.objects.get(pk=self.user.pk).use_sms)
        self.assertEqual(rep.resolver_match.func, manage_sms)

    def test_deactive_notifiaction_sms(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/manage_sms/', {'active': 'false'})
        self.assertEqual(rep.status_code, 200)
        self.assertFalse(rep.json()['actived'])
        self.assertFalse(User.objects.get(pk=self.user.pk).use_sms)
        self.assertEqual(rep.resolver_match.func, manage_sms)

    def test_active_notification_sms_fail(self):
        rep = self.cli.get('/manage_sms/')
        self.assertEqual(rep.status_code, 302)

    def test_remove_account(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/remove_account/', {'confirm': 'true'})
        self.assertEqual(rep.resolver_match.func, remove_account)
        self.assertRedirects(rep, '/')
        self.assertEqual(len(User.objects.all()), 0)

    def test_remove_account_fail(self):
        rep = self.cli.get('/remove_account/')
        self.assertEqual(rep.status_code, 302)

    def test_remove_account_fail_with_get(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.get('/remove_account/')
        self.assertEqual(rep.status_code, 200)
        self.assertFalse(rep.json()['success'])


class MethodUserModelTestCase(TestCase):

    def test_get_group_user_method(self):
        self.user = User.objects.create_user(
            'testOne',
            'emailTest@test.com',
            'testpassword',
            number=271235678
        )
        new_group = Group(name="Groupe pour test")
        new_group.save()
        perm1 = Permission.objects.get(codename='view_planningam')
        perm2 = Permission.objects.get(codename='view_planningpm')
        new_group.permissions.set([perm1, perm2])
        new_group.save()
        self.user.groups.add(new_group)
        self.assertEqual(self.user.get_group(), 'Groupe pour test')
