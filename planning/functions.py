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


def all_key_save(user):
    keys_save = []

    try:
        list_keys = SecretKeySave.objects.filter(users__id=user.id).values(
        'secret_key_saved',
        )
        for k in list_keys:
            k['username'] = User.objects.get(secret_key=k['secret_key_saved']).username
            keys_save.append(k)

    except AttributeError:
        keys_save.append(('Error', 'Erreur'))


    return keys_save
