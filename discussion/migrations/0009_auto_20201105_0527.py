# Generated by Django 3.1.1 on 2020-11-05 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_auto_20201102_2102'),
        ('discussion', '0008_auto_20201105_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.ForeignKey(default='', limit_choices_to={'profile': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_app.studentcourse'),
        ),
    ]
