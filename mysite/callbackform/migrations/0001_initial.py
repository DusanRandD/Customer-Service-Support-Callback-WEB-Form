# Generated by Django 3.2.6 on 2021-08-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('problem_description', models.TextField()),
            ],
        ),
    ]
