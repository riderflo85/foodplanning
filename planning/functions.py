from .models import Planning
import htmlmin


def check_user_planning(user):
    try:
        planning = Planning.objects.get(id_user=user.id)
        return planning
    except:
        return False


def display_planning(planning, user):
    plan = f"""<div class='container-fluid define-size-2 z-index-block'>
        <div class='row h-100'>
            <div class='col-12 col-lg-10 offset-lg-1 h-100' id='divContent'>
                <p class='lead text-white mt-5'>Planning pour {user.first_name}</p>
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
                            <td id='plat-lu-pl-1'{planning.monday} <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-ma-pl-1'>{planning.tuesday}</td>
                            <td id='plat-me-pl-1'>{planning.wednesday} <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-je-pl-1'>{planning.thursday}</td>
                            <td id='plat-ve-pl-1'>{planning.friday} <a href='#' class='badge badge-pill badge-warning text-secondary'>notif</a></td>
                            <td id='plat-sa-pl-1'>{planning.saturday}</td>
                            <td id='plat-di-pl-1'>{planning.sunday}</td>
                            <td><button type='button' class='btn btn-warning text-white'><i class='fas fa-bell'></i></button></td>
                        </tr>
                    </tbody>
                </table>
            </div><!-- end .col-12 -->
        </div><!-- end .row -->
    </div><!-- end .container-fluid -->"""
    return htmlmin.minify(plan)