from django.shortcuts import render
from django.contrib.auth.models import User
from .tasks import add


def planning(request):
    context = {}

    context['users'] = User.objects.all()

    return render(request, 'planning/index.html', context)

def testtask(request):
    context = {}
    task = add.delay(5, 5)
    context['testTask'] = task
    context['testTaskId'] = task.id
    context['testTaskStatus'] = task.status

    return render(request, 'planning/testtask.html', context)