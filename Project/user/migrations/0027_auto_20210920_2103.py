# Generated by Django 3.2.6 on 2021-09-20 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20210917_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazondata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 21, 3, 29, 364935)),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='flipkartdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 21, 3, 29, 365935)),
        ),
        migrations.AlterField(
            model_name='snapdealdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 21, 3, 29, 365935)),
        ),
    ]
