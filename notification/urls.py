from django.urls import path
from . import views


app_name = 'notification'
urlpatterns = [
    path('set/', views.set_notification, name='send_notification'),
]
