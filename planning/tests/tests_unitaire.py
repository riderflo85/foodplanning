from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from planning.functions import check_user_planning, display_planning
from planning.models import Planning


class UnitaireTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('userTest', 'testuser@test.com', 'PwdUserTest')
        self.user.first_name = 'test_first_name'
        self.user.save()
        planning = Planning()
        planning.monday = "Plat 1"
        planning.tuesday = "Plat 2"
        planning.wednesday = "Plat 3"
        planning.thursday = "Plat 4"
        planning.friday = "Plat 5"
        planning.saturday = "Plat 6"
        planning.sunday = "Plat 7"
        planning.moment_day = "am"
        planning.id_user = self.user
        planning.save()
        self.plann = planning

    def test_check_user_planning_function(self):
        rep = check_user_planning(self.user)
        self.assertEqual(rep, self.plann)

    def test_check_user_planning_function_fail(self):
        rep = check_user_planning('not_user')
        self.assertFalse(rep)

    def test_display_planning_function(self):
        rep = display_planning(self.plann, self.user)
        result = """<div class='container-fluid define-size-2 z-index-block'>
        <div class='row h-100'>
            <div class='col-12 col-lg-10 offset-lg-1 h-100' id='divContent'>
                <p class='lead text-white mt-5'>Planning pour test_first_name</p>
                <table class='table table-striped table-dark'>
                    <thead>
                        <tr>
                            <th scope='col'>Lundi</th>
                            <th scope='col'>Mardi</th>
                            <th scope='col'>Mercredi</th>
                            <th scope='col'>Jeudi</th>
                            <th scope='col'>Vendredi</th>
                            <th scope='col'>Samedi</th>
                            <th scope='col'>Dimanche</th>
                            <th scope='col'>#</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <select name='Lundi' class='custom-select' id='Lundi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Mardi' class='custom-select' id='Mardi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Mercredi' class='custom-select' id='Mercredi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Jeudi' class='custom-select' id='Jeudi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Vendredi' class='custom-select' id='Vendredi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Samedi' class='custom-select' id='Samedi-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <select name='Dimanche' class='custom-select' id='Dimanche-p'>
                                    <option selected>Choisissez un plât</option>
                                    <option value='croc'>croc monsieur</option>
                                    <option value='pate'>pate</option>
                                    <option value='patate'>patate</option>
                                    <option value='gratin'>gratin</option>
                                </select>
                            </td>
                            <td>
                                <div class='d-flex-inline'>
                                    <button type='button' class='btn btn-success' id='ValidPlanning'><i class='fas fa-check'></i></button>
                                    <button type='button' class='btn btn-primary' id='EditPlanning'><i class='fas fa-pencil-alt'></i></button>
                                    <button type='button' class='btn btn-danger' id='RemovePlanning'><i class='fas fa-trash-alt'></i></button>
                                </div>
                            </td>
                        </tr>
                        <tr class='text-center'>
                            <td id='plat-lu-pl-1'>Plat 1 <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-ma-pl-1'>Plat 2</td>
                            <td id='plat-me-pl-1'>Plat 3 <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-je-pl-1'>Plat 4</td>
                            <td id='plat-ve-pl-1'>Plat 5 <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-sa-pl-1'>Plat 6</td>
                            <td id='plat-di-pl-1'>Plat 7</td>
                            <td><button type='button' class='btn btn-warning text-white'><i class='fas fa-bell'></i></button></td>
                        </tr>
                    </tbody>
                </table>
            </div><!-- end .col-12 -->
        </div><!-- end .row -->
    </div><!-- end .container-fluid -->"""
        self.assertEqual(rep, mark_safe(result))