# Generated by Django 3.2.6 on 2021-09-12 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20210912_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipkartdata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 20, 24, 56, 377078)),
        ),
        migrations.AddField(
            model_name='snapdealdata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 20, 24, 56, 377078)),
        ),
        migrations.AlterField(
            model_name='amazondata',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 20, 24, 56, 377078)),
        ),
    ]
