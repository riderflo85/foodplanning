from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from usercontrol.models import User
from planning.models import PlanningAm, PlanningPm


def get_dish(request):
    """ Return the dish requested by the request on the API """

    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            day = request.POST['day']
            am_or_pm = request.POST['amOrPm']

            if am_or_pm == "am":
                plann = PlanningAm.objects.get(id_user=user.pk)
                dish = getattr(plann, day)
                return JsonResponse({"dish": dish})

            elif am_or_pm == "pm":
                plann = PlanningPm.objects.get(id_user=user.pk)
                dish = getattr(plann, day)
                return JsonResponse({"dish": dish})

        except ObjectDoesNotExist:
            return JsonResponse({"error": True})
