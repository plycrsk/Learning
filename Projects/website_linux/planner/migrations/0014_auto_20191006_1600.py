# Generated by Django 2.2.1 on 2019-10-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0013_auto_20191006_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
