# Generated by Django 2.1.5 on 2019-05-12 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gymobile_app', '0004_auto_20190512_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='data_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 17, 27, 23, 311723)),
        ),
    ]
