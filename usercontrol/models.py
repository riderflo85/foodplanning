from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    number = models.IntegerField(null=False)
    use_sms = models.BooleanField(default=False)

    def get_group(self):
        """ Return the name group """

        return self.groups.get().name
