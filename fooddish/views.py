from django.shortcuts import render
from .models import Fooddish

# Create your views here.
def index(request):
    context = {}

    list_dish = Fooddish.objects.all()
    context['list_dish'] = list_dish

    return render(request, 'fooddish/index.html', context)

def add_dish(request):
    pass