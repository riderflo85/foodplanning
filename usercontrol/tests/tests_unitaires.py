from django.test import TestCase
from usercontrol.keygen import key_generator


class KeyGenneratorTestCase(TestCase):

    def test_comparator_function(self):
        result = key_generator()
        self.assertEqual(len(result), 24)
        self.assertEqual(type(result), str)