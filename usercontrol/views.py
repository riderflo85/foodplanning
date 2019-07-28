from django.shortcuts import render
from .forms import SignupForm

def sign_in(request):
    return render(request, 'usercontrol/sign_in.html')

def sign_up(request):
    context = {}
    form = SignupForm()
    context['form'] = form

    return render(request, 'usercontrol/sign_up.html', context)