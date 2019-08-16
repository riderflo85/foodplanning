from django.urls import path
from . import views


app_name = 'planning'
urlpatterns = [
    path('', views.planning, name="planning"),
    path('set', views.create_planning_am, name="create_planning"),
]
