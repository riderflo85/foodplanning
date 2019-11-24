from django.test import TestCase, Client
from usercontrol.models import User


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user = User.objects.create_user(
            'usernameTest',
            'emailTest',
            'passwordTest',
            number=7223689,
        )
        self.cli.login(username=user.username, password='passwordTest')

    def test_page_set_notification(self):
        rep = self.cli.get('/notif/set')
        self.assertEqual(rep.status_code, 200)


class SetNotificationForUserTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        self.user = User.objects.create_user(
            'usernameTest',
            'emailTest',
            'passwordTest',
            number=7223689,
        )
        self.cli.login(username=self.user.username, password='passwordTest')

    def test_request_post_data_for_set_notification_fail(self):
        rep = self.cli.post('/notif/set', {
            'date': '2019-10-10',
            'time': '10:30',
            'message': 'Sortir le poulet du congélateur'
        })
        self.assertEqual(rep.json()['Response'], 'Notification disabled')
