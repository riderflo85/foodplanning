from .models import PlanningAm, PlanningPm
from usercontrol.models import User, SecretKeySave


def check_user_planning_am(user):
    try:
        planning = PlanningAm.objects.filter(id_user=user.id)
        return planning
    except:
        return False


def check_user_planning_pm(user):
    try:
        planning = PlanningPm.objects.filter(id_user=user.id)
        return planning
    except:
        return False


def list_key_save(user):
    keys_save = SecretKeySave.objects.filter(users__id=user.id)
    # A tester et a finir
    # doit retourner une liste de tuple -> (username, secret_key)