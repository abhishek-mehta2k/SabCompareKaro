# Generated by Django 3.2.6 on 2021-09-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_carddata_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecommerce', models.CharField(default='Amazon', editable=False, max_length=10)),
                ('image', models.ImageField(upload_to='card/')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CardData',
        ),
    ]
