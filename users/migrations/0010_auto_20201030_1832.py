# Generated by Django 3.1.1 on 2020-10-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Bio',
            new_name='bio',
        ),
    ]
