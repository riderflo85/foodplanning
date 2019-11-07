from django.test import TestCase
from fooddish.list_all_dish import list_all_dish
from fooddish.models import Fooddish


class ListingAllDishInDatabaseTestCase(TestCase):
    def setUp(self):
        dish1 = Fooddish()
        dish2 = Fooddish()
        dish1.name = 'Tacos'
        dish2.name = 'Wrap chicken'
        dish1.save()
        dish2.save()
        self.d1 = dish1
        self.d2 = dish2

    def test_list_all_dish_function(self):
        data = [
            ('default', 'Choisissez un plat'),
            (self.d1.pk, self.d1.name),
            (self.d2.pk, self.d2.name)
        ]
        result = list_all_dish()
        self.assertEqual(result, data)