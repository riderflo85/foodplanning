from django.test import TestCase
from notification.callr import convert_utc_datetime


class ConvertUtcDatetimeTestCase(TestCase):

    def test_convert_utc(self):
        """ Converts time and date to UTC """

        date = '2019-10-10'
        time = '10:30'
        result = convert_utc_datetime(time, date)
        self.assertEqual(str(result), '2019-10-10 08:30:00')