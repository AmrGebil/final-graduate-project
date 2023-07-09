# Generated by Django 4.1 on 2023-06-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='disease_knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desciption', models.TextField(max_length=1000)),
                ('treatment', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='first_aid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desciption', models.TextField(max_length=1000)),
                ('treatment', models.TextField(max_length=1000)),
            ],
        ),
    ]
