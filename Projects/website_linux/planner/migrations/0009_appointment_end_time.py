# Generated by Django 2.2.1 on 2019-10-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0008_remove_appointment_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(default='23:59'),
        ),
    ]