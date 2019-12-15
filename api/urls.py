from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('get', views.get, name="get"),
    path('get_today', views.get_today, name="get_today"),
]
