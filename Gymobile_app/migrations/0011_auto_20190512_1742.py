# Generated by Django 2.1.5 on 2019-05-12 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gymobile_app', '0010_auto_20190512_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 17, 42, 11, 130980)),
        ),
    ]