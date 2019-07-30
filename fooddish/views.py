from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Fooddish
from.forms import AddDishForms

# Create your views here.
def index(request):
    context = {}

    form = AddDishForms()
    list_dish = Fooddish.objects.all()
    context['list_dish'] = list_dish
    context['form'] = form

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
