from django.shortcuts import render
from django.http import JsonResponse
from .callr import convert_utc_datetime
from .tasks import send_notification
from usercontrol.models import PhoneNumber


def set_notification(request):
    context = {}

    if request.method == 'POST':
        if request.user.is_authenticated:
            date = request.POST['date']
            time = request.POST['time']
            msg = request.POST['message']
            num_user = PhoneNumber.objects.get(id_user=request.user).number
            comp_num = "".join(['+33', str(num_user)])

            result = convert_utc_datetime(time, date)
            task = send_notification.apply_async((comp_num, msg), eta=result)

            return JsonResponse({'Response': True})
        else:
            return JsonResponse({'Response': 'Not connect'})

    else:
        pass