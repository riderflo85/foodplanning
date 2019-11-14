from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    number = models.IntegerField(null=False)
    use_sms = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=28, null=False)


class SecretKeySave(models.Model):
    secret_key_saved = models.CharField(max_length=28, null=False)
    users = models.ForeignKey(User, on_delete=models.CASCADE)