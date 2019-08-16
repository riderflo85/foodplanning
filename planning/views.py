from django.shortcuts import render
from django.contrib.auth.models import User


def planning(request):
    context = {}

    context['users'] = User.objects.all()

    return render(request, 'planning/index.html', context)
