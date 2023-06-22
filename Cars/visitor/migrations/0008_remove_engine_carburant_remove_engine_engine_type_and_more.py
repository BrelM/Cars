# Generated by Django 4.2.2 on 2023-06-22 20:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_last_login_alter_user_password'),
        ('visitor', '0007_rename_nbseats_cartype_nb_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engine',
            name='carburant',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='power',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='car',
        ),
        migrations.AddField(
            model_name='announcement',
            name='builder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.builder'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.cartype'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='carburant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.carburant'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='color',
            field=models.CharField(default='No color provided', max_length=100),
        ),
        migrations.AddField(
            model_name='announcement',
            name='engine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.enginetype'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='announcement',
            name='model',
            field=models.CharField(default='new model', max_length=200),
        ),
        migrations.AddField(
            model_name='announcement',
            name='nb_horses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='announcement',
            name='power',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.powertype'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='speed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='visitor.speedtype'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='state',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='announcement',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Engine',
        ),
    ]