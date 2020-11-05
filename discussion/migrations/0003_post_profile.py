# Generated by Django 3.1.1 on 2020-11-05 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20201030_1832'),
        ('discussion', '0002_post_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
