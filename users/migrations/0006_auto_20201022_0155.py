# Generated by Django 3.1.1 on 2020-10-22 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201022_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='course1',
            new_name='course_1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='course2',
            new_name='course_2',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='course3',
            new_name='course_3',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='course4',
            new_name='course_4',
        ),
    ]