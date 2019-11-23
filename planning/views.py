from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test
from usercontrol.models import User
from fooddish.models import Fooddish
from .models import PlanningAm, PlanningPm
from .functions import check_user_planning_am, check_user_planning_pm


def planning(request):
    context = {}

    if request.user.is_authenticated:
        weeks = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        users = User.objects.filter(groups=request.user.groups.get())
        group_users = users.exclude(username=request.user.username)
        context['days'] = weeks
        context['users'] = users
        context['group_users'] = group_users
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
        users = User.objects.filter(groups=request.user.groups.get())
        group_users = users.exclude(username=request.user.username)
        context['days'] = weeks
        context['users'] = users
        context['group_users'] = group_users
        dico_dishs = {}
        all_dishs = Fooddish.objects.all()

        for i in all_dishs:
            dico_dishs[i.id] = i
        
        context['dishs'] = dico_dishs

        planning = check_user_planning_pm(request.user)
        context['planning'] = planning

    return render(request, 'planning/pm.html', context)


def create_planning(request):
    try:
        if request.POST['momentDay'] == 'am':
            new_planning = PlanningAm()
        elif request.POST['momentDay'] == 'pm':
            new_planning = PlanningPm()

        for key in request.POST:
            if key == 'momentDay':
                pass
            else:
                setattr(new_planning, key, request.POST[key])

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

        for key in request.POST:
            if key == "momentDay" or key == "id":
                pass
            else:
                if not request.POST[key].startswith('Plat actuel:'):
                    setattr(
                        planning,
                        key,
                        Fooddish.objects.get(id=int(request.POST[key])).name
                    )
        planning.save()

        return JsonResponse({'ServeurResponse': True})

def check_permission_am(user):
    return user.has_perm('planning.view_planningam')

def check_permission_pm(user):
    return user.has_perm('planning.view_planningpm')

@user_passes_test(check_permission_am, login_url='/')
def another_planning_am(request):
    try:
        other_user = User.objects.get(pk=request.POST['selectUser'])
        another_planning = PlanningAm.objects.get(id_user=other_user.id)
        context = {
            'planning': another_planning,
            'planning_exist': True,
            'other_user': other_user
        }

    except ObjectDoesNotExist:
        context = {'planning_exist': False}

    return render(request, 'planning/another_planning_am.html', context)


@user_passes_test(check_permission_pm, login_url='/')
def another_planning_pm(request):
    try:
        other_user = User.objects.get(pk=request.POST['selectUser'])
        another_planning = PlanningPm.objects.get(id_user=other_user.id)
        context = {
            'planning': another_planning,
            'planning_exist': True,
            'other_user': other_user
        }

    except ObjectDoesNotExist:
        context = {'planning_exist': False}

    return render(request, 'planning/another_planning_pm.html', context)