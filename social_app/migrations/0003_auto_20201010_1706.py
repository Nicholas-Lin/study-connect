# Generated by Django 3.1.2 on 2020-10-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_auto_20201010_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meeting_days',
            field=models.CharField(max_length=7),
        ),
    ]
