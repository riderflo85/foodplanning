from .models import Planning


def check_user_planning(user):
    try:
        planning = Planning.objects.filter(id_user=user.id)
        return planning
    except:
        return False
