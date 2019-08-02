from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Fooddish
from.forms import AddDishForms, DelDishForms

# Create your views here.
def index(request):
    context = {}

    form = AddDishForms()
    form_select = DelDishForms()
    list_dish = Fooddish.objects.all()
    context['list_dish'] = list_dish
    context['form'] = form
    context['form_select'] = form_select

    return render(request, 'fooddish/index.html', context)

def add_dish(request):
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
        pass

def delete_dish(request):
    if request.method == 'POST':
        form = DelDishForms(request.POST)

        if form.is_valid():
            del_dish = form.cleaned_data['del_dish']
            dish = Fooddish.objects.get(pk=del_dish)
            dish.delete()
            return redirect(reverse('fooddish:liste_des_plats'))

        else:
            return redirect(reverse('fooddish:liste_des_plats'))

    else:
        pass

def all_dish(request):
    if request.method == 'GET':
        list_dish = []
        dishs = Fooddish.objects.all()

        for i in dishs:
            list_dish.append(i.name)
    
    return JsonResponse({'Data': list_dish})