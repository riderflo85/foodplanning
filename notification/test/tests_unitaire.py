from django.test import TestCase
from unittest.mock import patch
from notification.callr import convert_utc_datetime
from notification.tasks import send_notification


class ConvertUtcDatetimeTestCase(TestCase):

    def test_convert_utc(self):
        """ Converts time and date to UTC """

        date = '2019-10-10'
        time = '10:30'
        result = convert_utc_datetime(time, date)
        self.assertEqual(str(result), '2019-10-10 08:30:00')


class SendSmsTestCase(TestCase):

    @patch('callr.Api.call')
    def test_send_sms_with_callr_api(self, mock_send_notification):
        number = '+33741259865'
        message = 'Sms de test'

        mock_send_notification.return_value = "DE1248FT"
        id_sms = send_notification(number, message)

        self.assertEqual(id_sms, "DE1248FT")
