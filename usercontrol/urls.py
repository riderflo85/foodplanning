from django.urls import path
from . import views


app_name = 'usercontrol'
urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
]
