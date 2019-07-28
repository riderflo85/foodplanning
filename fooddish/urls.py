from django.urls import path
from . import views


app_name = 'fooddish'
urlpatterns = [
    path('', views.index, name='liste_des_plats'),
]
