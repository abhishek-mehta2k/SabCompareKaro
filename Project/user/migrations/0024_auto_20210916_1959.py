# Generated by Django 3.2.6 on 2021-09-16 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20210916_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazondata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 59, 49, 216995)),
        ),
        migrations.AlterField(
            model_name='flipkartdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 59, 49, 216995)),
        ),
        migrations.AlterField(
            model_name='snapdealdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 59, 49, 216995)),
        ),
    ]