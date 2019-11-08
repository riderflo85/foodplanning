from django.test import TestCase
from notification.callr import convert_utc_datetime, api
from notification.tasks import send_notification

class ConvertUtcDatetimeTestCase(TestCase):

    def test_convert_utc(self):
        """ Converts time and date to UTC """

        date = '2019-10-10'
        time = '10:30'
        result = convert_utc_datetime(time, date)
        self.assertEqual(str(result), '2019-10-10 08:30:00')

# class SendSmsTestCase(TestCase):

#     def test_send_sms_with_callr_api(self, monkeypatch):
#         number = '+33741259865'
#         message = 'Sms de test'
#         result = "DE1248FT"

#         def mock_callr(method, type, num, sms, encode):
#             return result

#         monkeypatch.setattr(api, 'call', mock_callr)

#         id_sms = send_notification(number, message)
#         self.assertEqual(id_sms, result)