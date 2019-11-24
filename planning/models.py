from django.db import models
from usercontrol.models import User


class PlanningAm(models.Model):
    monday = models.CharField(max_length=160)
    tuesday = models.CharField(max_length=160)
    wednesday = models.CharField(max_length=160)
    thursday = models.CharField(max_length=160)
    friday = models.CharField(max_length=160)
    saturday = models.CharField(max_length=160)
    sunday = models.CharField(max_length=160)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    notif_mo = models.BooleanField(default=False)
    notif_tu = models.BooleanField(default=False)
    notif_we = models.BooleanField(default=False)
    notif_th = models.BooleanField(default=False)
    notif_fr = models.BooleanField(default=False)
    notif_sa = models.BooleanField(default=False)
    notif_su = models.BooleanField(default=False)
    text_notif_mo = models.TextField(null=True)
    text_notif_tu = models.TextField(null=True)
    text_notif_we = models.TextField(null=True)
    text_notif_th = models.TextField(null=True)
    text_notif_fr = models.TextField(null=True)
    text_notif_sa = models.TextField(null=True)
    text_notif_su = models.TextField(null=True)

    class Meta:
        verbose_name = "Planning du midi de la semaine"

    def __str__(self):
        return f"planning du midi de {self.id_user}"


class PlanningPm(models.Model):
    monday = models.CharField(max_length=160)
    tuesday = models.CharField(max_length=160)
    wednesday = models.CharField(max_length=160)
    thursday = models.CharField(max_length=160)
    friday = models.CharField(max_length=160)
    saturday = models.CharField(max_length=160)
    sunday = models.CharField(max_length=160)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    notif_mo = models.BooleanField(default=False)
    notif_tu = models.BooleanField(default=False)
    notif_we = models.BooleanField(default=False)
    notif_th = models.BooleanField(default=False)
    notif_fr = models.BooleanField(default=False)
    notif_sa = models.BooleanField(default=False)
    notif_su = models.BooleanField(default=False)
    text_notif_mo = models.TextField(null=True)
    text_notif_tu = models.TextField(null=True)
    text_notif_we = models.TextField(null=True)
    text_notif_th = models.TextField(null=True)
    text_notif_fr = models.TextField(null=True)
    text_notif_sa = models.TextField(null=True)
    text_notif_su = models.TextField(null=True)

    class Meta:
        verbose_name = "Planning du soir de la semaine"

    def __str__(self):
        return f"planning du soir de {self.id_user}"
