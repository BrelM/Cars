# Generated by Django 4.2.2 on 2023-06-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default='xxx', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='xx', max_length=200),
        ),
    ]
