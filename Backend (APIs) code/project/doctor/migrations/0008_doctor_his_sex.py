# Generated by Django 4.1 on 2023-02-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_doctor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='his_sex',
            field=models.CharField(choices=[('ذكر', 'ذكر'), ('انثي', 'انثي')], default='Notfound', max_length=15),
        ),
    ]
