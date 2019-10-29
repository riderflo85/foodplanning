from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from .models import PhoneNumber, NotificationBySms
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

            new_user = User.objects.create_user(pseudo, email, pwd)
            new_user.last_name = last_name
            new_user.first_name = first_name
            new_user.save()
            phone_number = PhoneNumber()
            phone_number.number = phone
            phone_number.id_user = new_user
            phone_number.save()
            notification_sms = NotificationBySms()
            notification_sms.id_user = new_user
            notification_sms.save()
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
        context = {}
        try:
            context['phone'] = PhoneNumber.objects.get(
                id_user=request.user.pk
            ).number
            context['use_sms'] = NotificationBySms.objects.get(
                id_user=request.user.pk
            ).use_sms
        except:
            pass

        return render(request, 'usercontrol/account.html', context)
    else:
        return redirect(reverse('usercontrol:sign_in'))

def edit_user_infos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                user = request.user
                phone_user = PhoneNumber.objects.get(id_user=user.pk)
                user_infos = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'pseudo': user.username,
                    'email': user.email,
                    'phone': phone_user.number
                }

                if comparator(user_infos['last_name'], request.POST['last_name']):
                    user.last_name = request.POST['last_name']

                if comparator(user_infos['first_name'], request.POST['first_name']):
                    user.first_name = request.POST['first_name']

                if comparator(user_infos['pseudo'], request.POST['pseudo']):
                    user.username = request.POST['pseudo']

                if comparator(user_infos['email'], request.POST['email']):
                    user.email = request.POST['email']

                if comparator(user_infos['phone'], request.POST['phone'][1:]):
                    phone_user.number = int(request.POST['phone'][1:])

                user.save()
                phone_user.save()
                return JsonResponse({'success': True})

            except:
                return JsonResponse({'success': False})
    else:
        return redirect(reverse('usercontrol:sign_in'))

def changePasswd(request):
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
            try:
                user = NotificationBySms.objects.get(id_user=request.user)

                if request.POST['active'] == True:
                    user.use_sms = True
                    user.save()

                elif request.POST['active'] == False:
                    user.use_sms = False
                    user.save()

                return JsonResponse({'actived': True})

            except:
                return JsonResponse({'actived': False})
    else:
        return redirect(reverse('usercontrol:sign_in'))