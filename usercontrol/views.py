from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from .models import User
from .comparator import comparator


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
                return redirect(reverse('planning:planning'))
            else:
                context['error'] = True
    else:
        form = LoginForm()

    context['form'] = form

    return render(request, 'usercontrol/sign_in.html', context)

def sign_up(request):
    context = {'error': False}
    confirm = False

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            phone = form.cleaned_data['phone_number']

            new_user = User.objects.create_user(pseudo, email, pwd, number=phone)
            new_user.last_name = last_name
            new_user.first_name = first_name
            new_user.save()
            confirm = True
        else:
            context['error'] = form.errors.items()
        
        if confirm:
            return redirect(reverse('usercontrol:sign_in'))
        else:
            pass

    else:
        form = SignupForm()

    context['form'] = form

    return render(request, 'usercontrol/sign_up.html', context)

def sign_out(request):
    logout(request)

    return redirect(reverse('usercontrol:sign_in'))

def account(request):
    if request.user.is_authenticated:
        return render(request, 'usercontrol/account.html')
    else:
        return redirect(reverse('usercontrol:sign_in'))

def edit_user_infos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                data = request.POST
                user = User.objects.get(pk=request.user.pk)

                for k, v in request.POST.items():
                    if k == 'number':  
                        setattr(user, k, int(v))
                    else:
                        setattr(user, k, v)

                user.save()
                return JsonResponse({'success': True})

            except:
                return JsonResponse({'success': False})
    else:
        return redirect(reverse('usercontrol:sign_in'))

def change_passwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                user = request.user
                user.set_password(request.POST['new_pwd'])
                user.save()
                return JsonResponse({'success': True})

            except:
                return JsonResponse({'success': False})

    else:
        return redirect(reverse('usercontrol:sign_in'))

def manage_sms(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(pk=request.user.pk)

            if request.POST['active'] == 'true':
                user.use_sms = True
                user.save()
                return JsonResponse({'actived': True})

            elif request.POST['active'] == 'false':
                user.use_sms = False
                user.save()
                return JsonResponse({'actived': False})

    else:
        return redirect(reverse('usercontrol:sign_in'))

def remove_account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(pk=request.user.pk)

            if request.POST['confirm'] == 'true':
                user.delete()
                logout(request)
                
                return redirect(reverse('usercontrol:sign_in'))
        else:
            return JsonResponse({'success': False})
    else:
        return redirect(reverse('usercontrol:sign_in'))
