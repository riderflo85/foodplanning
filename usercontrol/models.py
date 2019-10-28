from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PhoneNumber(models.Model):
    number = models.IntegerField(null=False)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)


class NotificationBySms(models.Model):
    use_sms = models.BooleanField(default=False)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)