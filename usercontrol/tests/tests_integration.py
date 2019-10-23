from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from usercontrol.forms import SignupForm, LoginForm
from usercontrol.views import sign_in, sign_up, sign_out, account, edit_user_infos
from usercontrol.models import PhoneNumber


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
            password='longpasswordtest'
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.user = user_test

    def test_user_redirect_after_sign_in(self):
        data_for_login = {'user': 'testUser', 'password': 'longpasswordtest'}
        rep = self.cli.post('/', data_for_login)
        self.assertEqual(rep.status_code, 302)

    def test_user_sign_out(self):
        self.cli.login(username=self.user.username,
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
            'phone_number': 670217836
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
            'phone_number': 670217836
        }
        rep = self.cli.post('/sign_up/', data)
        self.assertFormError(rep, 'form', 'email', 'Saisissez une adresse de courriel valide.')


class FormTestCase(TestCase):
    def test_form_sign_up(self):
        form_data = {
            'pseudo': 'testUser',
            'last_name': 'FooTest',
            'first_name': 'Tester',
            'email': 'testuser@founisseur.com',
            'password': 'longpasswordtest',
            'phone_number': '770207030'
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
            password='test'
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
            password='testpassword'
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        phone = PhoneNumber()
        phone.id_user = user_test
        phone.number = 773450857
        phone.save()
        self.data = {
            'last_name': 'lastNameTest',
            'first_name': 'firstNameTest',
            'pseudo': 'pseudoForTest',
            'email': 'emailtest@test.com',
            'phone': '071235678',
        }
        self.user = user_test

    def test_change_user_infos(self):
        self.cli.login(username=self.user.username, password='testpassword')
        rep = self.cli.post('/edit_infos/', self.data)
        self.assertEqual(rep.resolver_match.func, edit_user_infos)
        self.assertTrue(rep.json()['success'])
        rep2 = self.cli.get('/account/')
        self.assertEqual(rep.status_code, 200)

    def test_change_user_infos_fail(self):
        rep = self.cli.post('/edit_infos/', self.data)
        self.assertEqual(rep.status_code, 302)
