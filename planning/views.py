from django.shortcuts import render

# Create your views here.
def planning(request):
    return render(request, 'planning/index.html')