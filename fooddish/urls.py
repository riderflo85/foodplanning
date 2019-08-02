from django.urls import path
from . import views


app_name = 'fooddish'
urlpatterns = [
    path('', views.index, name='liste_des_plats'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('delete_dish/', views.delete_dish, name='delete_dish'),
    path('all_dish/', views.all_dish, name='all_dish'),
]
