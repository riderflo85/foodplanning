from .models import PlanningAm


def check_user_planning(user):
    try:
        planning = PlanningAm.objects.filter(id_user=user.id)
        return planning
    except:
        return False
