from django.test import TestCase
from usercontrol.comparator import comparator


class ComparatorTestCase(TestCase):
    def setUp(self):
        self.old_data = "oldUsername"
        self.new_data = "newUsername"
        self.not_data = ""

    def test_comparator_function(self):
        result1 = comparator(self.old_data, self.new_data)
        self.assertTrue(result1)

        result2 = comparator(self.old_data, self.not_data)
        self.assertFalse(result2)