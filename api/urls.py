from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('v1/dish', views.get_dish, name="dish"),
]
