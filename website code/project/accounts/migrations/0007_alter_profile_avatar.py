# Generated by Django 4.1 on 2023-07-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_images'),
        ),
    ]
