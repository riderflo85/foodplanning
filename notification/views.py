from django.http import JsonResponse
from .callr import convert_utc_datetime
from .tasks import send_notification
from usercontrol.models import User


def set_notification(request):
    """ Added a send sms task """

    req_user = request.user
    user = User.objects.get(pk=req_user.pk)

    if request.method == 'POST':
        if req_user.is_authenticated is True and user.use_sms is True:
            date = request.POST['date']
            time = request.POST['time']
            msg = request.POST['message']
            num_user = User.objects.get(pk=request.user.pk).number
            comp_num = "".join(['+33', str(num_user)])

            result = convert_utc_datetime(time, date)
            send_notification.apply_async((comp_num, msg), eta=result)

            return JsonResponse({'Success': True})
        else:
            return JsonResponse({'Response': 'Notification disabled'})

    else:
        return JsonResponse({'error': True})
