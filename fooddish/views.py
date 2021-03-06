from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Fooddish
from .forms import AddDishForms, DelDishForms


def index(request):
    """ Display all dishes of the database """

    context = {}

    form = AddDishForms()
    form_select = DelDishForms()
    list_dish = Fooddish.objects.all()
    context['list_dish'] = list_dish
    context['form'] = form
    context['form_select'] = form_select

    return render(request, 'fooddish/index.html', context)


def add_dish(request):
    """ Added new dish in the database """

    if request.method == 'POST':
        form = AddDishForms(request.POST)

        if form.is_valid():
            new_dish = form.cleaned_data['name_dish']
            adding_dish = Fooddish()
            adding_dish.name = new_dish
            adding_dish.save()
            return redirect(reverse('fooddish:liste_des_plats'))

        else:
            return redirect(reverse('fooddish:liste_des_plats'))
    else:
        return JsonResponse({'error': True})


def delete_dish(request):
    """ Deleted dish in the database """

    if request.method == 'POST':
        data = request.POST['id']
        try:
            Fooddish.objects.get(pk=int(data)).delete()
            return JsonResponse({'removed': True})

        except:
            return JsonResponse({'removed': False})
    else:
        return JsonResponse({'removed': False})


def all_dish(request):
    """ Return a list that contains all dishes of the database """

    if request.method == 'GET':
        dishes = Fooddish.objects.all().values('name')

    return JsonResponse({'Data': list(dishes)})
