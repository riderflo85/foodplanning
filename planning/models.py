from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Planning(models.Model):
    monday = models.CharField(max_length=160)
    tuesday = models.CharField(max_length=160)
    wednesday = models.CharField(max_length=160)
    thursday = models.CharField(max_length=160)
    friday = models.CharField(max_length=160)
    saturday = models.CharField(max_length=160)
    sunday = models.CharField(max_length=160)
    moment_day = models.CharField(max_length=2, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Planning de la semaine"

    def __str__(self):
        return f"planning de {self.id_user}"