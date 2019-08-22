from django.urls import path
from . import views


app_name = 'planning'
urlpatterns = [
    path('', views.planning, name="planning"),
    path('set', views.create_planning_am, name="create_planning"),
    path('remove', views.remove_planning_am, name="remove_planning"),
    path('update', views.update_planning_am, name="update_planning"),
]
