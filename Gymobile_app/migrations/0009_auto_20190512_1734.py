# Generated by Django 2.1.5 on 2019-05-12 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gymobile_app', '0008_auto_20190512_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 17, 34, 20, 656961)),
        ),
    ]