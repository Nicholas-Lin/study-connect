# Generated by Django 3.1.1 on 2020-11-05 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_auto_20201102_2102'),
        ('discussion', '0003_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.ForeignKey(default='', limit_choices_to={'profile': models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_app.studentcourse'),
        ),
    ]