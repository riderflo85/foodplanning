# Generated by Django 2.2.5 on 2019-11-19 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercontrol', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='secret_key',
        ),
        migrations.DeleteModel(
            name='SecretKeySave',
        ),
    ]
