from django.shortcuts import render
from usercontrol.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from .models import PlanningAm, PlanningPm
from fooddish.models import Fooddish
from .functions import check_user_planning_am, check_user_planning_pm


def planning(request):
    context = {}

    if request.user.is_authenticated:
        weeks = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        context['days'] = weeks
        context['users'] = User.objects.all()
        dico_dishs = {}
        all_dishs = Fooddish.objects.all()

        for i in all_dishs:
            dico_dishs[i.id] = i
        
        context['dishs'] = dico_dishs

        planning = check_user_planning_am(request.user)
        context['planning'] = planning

    return render(request, 'planning/index.html', context)


def planning_pm(request):
    context = {}

    if request.user.is_authenticated:
        weeks = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        context['days'] = weeks
        context['users'] = User.objects.all()
        dico_dishs = {}
        all_dishs = Fooddish.objects.all()

        for i in all_dishs:
            dico_dishs[i.id] = i
        
        context['dishs'] = dico_dishs

        planning = check_user_planning_pm(request.user)
        context['planning'] = planning

    return render(request, 'planning/pm.html', context)


def create_planning(request):
    dico_dishs = {}

    try:
        if request.POST['momentDay'] == 'am':
            new_planning = PlanningAm()
        elif request.POST['momentDay'] == 'pm':
            new_planning = PlanningPm()

        for i in request.POST:
            dico_dishs[i] = request.POST[i]
    
        new_planning.monday = dico_dishs['days1']
        new_planning.tuesday = dico_dishs['days2']
        new_planning.wednesday = dico_dishs['days3']
        new_planning.thursday = dico_dishs['days4']
        new_planning.friday = dico_dishs['days5']
        new_planning.saturday = dico_dishs['days6']
        new_planning.sunday = dico_dishs['days7']
        new_planning.id_user = request.user
        new_planning.save()
        error_db = False
        validate = True

    except IntegrityError:
        error_db = True
        validate = False

    data_response = {
        'ServeurResponse': validate,
        'id_planning': new_planning.pk,
        'error': error_db
    }
    return JsonResponse(data_response)

def remove_planning(request):
    if request.method == 'POST':
        id_planning = request.POST['id_planning']
        moment_day = request.POST['momentDay']

        if moment_day == 'am':
            PlanningAm.objects.get(id=int(id_planning)).delete()
        elif moment_day == 'pm':
            PlanningPm.objects.get(id=int(id_planning)).delete()

        return JsonResponse({'ServeurResponse': True})
    else:
        return JsonResponse({'ServeurResponse': False})


def update_planning(request):
    if request.method == 'POST':
        moment_day = request.POST['momentDay']

        if moment_day == 'am':
            planning = PlanningAm.objects.get(id=int(request.POST['id']))
        elif moment_day == 'pm':
            planning = PlanningPm.objects.get(id=int(request.POST['id']))

        planning.monday = Fooddish.objects.get(id=int(request.POST['monday'])).name
        planning.tuesday = Fooddish.objects.get(id=int(request.POST['tuesday'])).name
        planning.wednesday = Fooddish.objects.get(id=int(request.POST['wednesday'])).name
        planning.thursday = Fooddish.objects.get(id=int(request.POST['thursday'])).name
        planning.friday = Fooddish.objects.get(id=int(request.POST['friday'])).name
        planning.saturday = Fooddish.objects.get(id=int(request.POST['saturday'])).name
        planning.sunday = Fooddish.objects.get(id=int(request.POST['sunday'])).name
        planning.save()

        return JsonResponse({'ServeurResponse': True})