from django.shortcuts import render

def sign_in(request):
    return render(request, 'usercontrol/sign_in.html')

def sign_up(request):
    return render(request, 'usercontrol/sign_up.html')