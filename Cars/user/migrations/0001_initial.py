# Generated by Django 4.2.2 on 2023-06-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(default='xx', max_length=200)),
                ('login', models.CharField(default='xxx', max_length=200, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
