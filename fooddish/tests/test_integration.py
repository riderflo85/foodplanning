from django.test import TestCase, Client
from fooddish.forms import AddDishForms, DelDishForms
from fooddish.models import Fooddish


class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_index(self):
        rep = self.cli.get('/liste_des_plats/')
        self.assertEqual(rep.status_code, 200)

    def test_page_add_dish(self):
        rep = self.cli.get('/liste_des_plats/add_dish/')
        self.assertEqual(rep.status_code, 200)
        self.assertTrue(rep.json()['error'])

    def test_page_delete_dish(self):
        rep = self.cli.get('/liste_des_plats/delete_dish/')
        self.assertEqual(rep.status_code, 200)
        self.assertFalse(rep.json()['removed'])

    def test_page_all_dish(self):
        rep = self.cli.get('/liste_des_plats/all_dish/')
        self.assertEqual(rep.status_code, 200)


class ManageDishDatabaseTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        dish1 = Fooddish()
        dish2 = Fooddish()
        dish1.name = 'Patate au four'
        dish1.save()
        dish2.name = 'Poulet frite'
        dish2.save()
        self.d1 = dish1
        self.d2 = dish2

    def test_list_all_dish_view(self):
        rep = self.cli.get('/liste_des_plats/all_dish/')
        data = [
            {'name': self.d1.name},
            {'name': self.d2.name}
        ]
        self.assertEqual(rep.json()['Data'], data)

    def test_add_dish_in_database(self):
        data_post = {'name_dish': 'Tacos'}
        rep = self.cli.post('/liste_des_plats/add_dish/', data_post)
        self.assertRedirects(rep, '/liste_des_plats/')
        self.assertEqual(len(Fooddish.objects.all()), 3)

    def test_add_dish_in_database_fail(self):
        data_post = {'error_field_name': 'Tacos'}
        rep = self.cli.post('/liste_des_plats/add_dish/', data_post)
        self.assertRedirects(rep, '/liste_des_plats/')
        self.assertEqual(len(Fooddish.objects.all()), 2)

    def test_delete_dish_in_database(self):
        data_post = {'id': self.d1.pk}
        rep = self.cli.post('/liste_des_plats/delete_dish/', data_post)
        self.assertTrue(rep.json()['removed'])
        self.assertEqual(len(Fooddish.objects.all()), 1)

    def test_delete_dish_in_database_fail(self):
        data_post = {'id': '45'} # this id does not exist
        rep = self.cli.post('/liste_des_plats/delete_dish/', data_post)
        self.assertFalse(rep.json()['removed'])
        self.assertEqual(len(Fooddish.objects.all()), 2)