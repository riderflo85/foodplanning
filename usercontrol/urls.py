from django.urls import path
from . import views


app_name = 'usercontrol'
urlpatterns = [
    path('', views.sign_in, name="sign_in"),
]
