# Generated by Django 2.2.1 on 2019-10-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_appointment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='12:00'),
        ),
    ]