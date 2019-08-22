from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Planning
from fooddish.models import Fooddish


def planning(request):
    context = {}
    weeks = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    context['days'] = weeks
    context['users'] = User.objects.all()
    dico_dishs = {}
    all_dishs = Fooddish.objects.all()

    for i in all_dishs:
        dico_dishs[i.id] = i
    
    context['dishs'] = dico_dishs

    return render(request, 'planning/index.html', context)


def create_planning_am(request):
    dico_dishs = {}
    new_planning = Planning()
    for i in request.POST:
        dico_dishs[i] = request.POST[i]
    
    new_planning.monday = dico_dishs['days1']
    new_planning.tuesday = dico_dishs['days2']
    new_planning.wednesday = dico_dishs['days3']
    new_planning.thursday = dico_dishs['days4']
    new_planning.friday = dico_dishs['days5']
    new_planning.saturday = dico_dishs['days6']
    new_planning.sunday = dico_dishs['days7']
    new_planning.moment_day = 'am'
    new_planning.id_user = request.user
    new_planning.save()

    data_response = {'ServeurResponse': True, 'id_planning': new_planning.pk}
    return JsonResponse(data_response)


def create_planning_pm(request):
    dico_dishs = {}
    new_planning = Planning()
    for i in request.POST:
        dico_dishs[i] = request.POST[i]
    
    new_planning.monday = dico_dishs['days1']
    new_planning.tuesday = dico_dishs['days2']
    new_planning.wednesday = dico_dishs['days3']
    new_planning.thursday = dico_dishs['days4']
    new_planning.friday = dico_dishs['days5']
    new_planning.saturday = dico_dishs['days6']
    new_planning.sunday = dico_dishs['days7']
    new_planning.moment_day = 'pm'
    new_planning.id_user = request.user
    new_planning.save()

    data_response = {'ServeurResponse': True, 'id_planning': new_planning.pk}
    return JsonResponse(data_response)

def remove_planning_am(request):
    if request.method == 'POST':
        id_planning = request.POST['id_planning']
        Planning.objects.get(id=int(id_planning)).delete()
        return JsonResponse({'ServeurResponse': True})
    else:
        return JsonResponse({'ServeurResponse': False})        


def update_planning_am(request):
    if request.method == 'POST':
        planning = Planning.objects.get(id=int(request.POST['id']))
        planning.monday = Fooddish.objects.get(id=int(request.POST['monday'])).name
        planning.tuesday = Fooddish.objects.get(id=int(request.POST['tuesday'])).name
        planning.wednesday = Fooddish.objects.get(id=int(request.POST['wednesday'])).name
        planning.thursday = Fooddish.objects.get(id=int(request.POST['thursday'])).name
        planning.friday = Fooddish.objects.get(id=int(request.POST['friday'])).name
        planning.saturday = Fooddish.objects.get(id=int(request.POST['saturday'])).name
        planning.sunday = Fooddish.objects.get(id=int(request.POST['sunday'])).name
        planning.save()

        return JsonResponse({'ServeurResponse': True})