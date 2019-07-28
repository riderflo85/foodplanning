from django.shortcuts import render
from .forms import SignupForm, LoginForm

def sign_in(request):
    context = {}
    form = LoginForm()
    context['form'] = form

    return render(request, 'usercontrol/sign_in.html', context)

def sign_up(request):
    context = {}
    form = SignupForm()
    context['form'] = form

    return render(request, 'usercontrol/sign_up.html', context)