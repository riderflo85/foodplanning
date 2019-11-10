from django.urls import path
from . import views


app_name = 'planning'
urlpatterns = [
    path('', views.planning, name="planning"),
    path('pm', views.planning_pm, name="pm"),
    path('set', views.create_planning, name="create_planning"),
    path('remove', views.remove_planning, name="remove_planning"),
    path('update', views.update_planning, name="update_planning"),
    # Ajouter une nouvelle url pour consulter le planning d'un autre utilisateur
]
