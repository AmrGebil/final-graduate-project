# Generated by Django 4.1 on 2023-02-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_his_clinic_finsh_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='his_clinic_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='his_name',
            field=models.CharField(max_length=100),
        ),
    ]
