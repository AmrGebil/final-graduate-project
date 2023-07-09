# Generated by Django 4.1 on 2023-02-21 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='his_age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(200)]),
        ),
    ]
