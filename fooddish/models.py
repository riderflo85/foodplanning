from django.db import models


class Fooddish(models.Model):
    name = models.CharField(max_length=160, null=False, unique=True)

    class Meta:
        verbose_name = 'Plat'

    def __str__(self):
        return self.name