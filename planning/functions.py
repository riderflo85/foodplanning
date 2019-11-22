from .models import PlanningAm, PlanningPm


def check_user_planning_am(user):
    try:
        planning = PlanningAm.objects.get(id_user=user.id)
        return planning
    except:
        return False


def check_user_planning_pm(user):
    try:
        planning = PlanningPm.objects.get(id_user=user.id)
        return planning
    except:
        return False
