# Generated by Django 3.2.6 on 2021-09-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210912_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazondata',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='amazondata',
            name='created_time',
            field=models.TimeField(auto_now=True),
        ),
    ]