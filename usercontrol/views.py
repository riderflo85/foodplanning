from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm

def sign_in(request):
    context = {'error': False,}

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user']
            pwd = form.cleaned_data['password']
            login_user = authenticate(request, username=username, password=pwd)
            context['user'] = login_user

            if login_user is not None:
                login(request, user=login_user)
                return redirect(reverse('planning:index'))
            else:
                context['error'] = True
    else:
        form = LoginForm()

    context['form'] = form

    return render(request, 'usercontrol/sign_in.html', context)

def sign_up(request):
    context = {}
    form = SignupForm()
    context['form'] = form

    return render(request, 'usercontrol/sign_up.html', context)