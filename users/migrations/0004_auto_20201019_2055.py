# Generated by Django 3.1.1 on 2020-10-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year_in_school',
            field=models.CharField(blank=True, choices=[('1st', 'First-Year'), ('2nd', 'Second-Year'), ('3rd', 'Third-Year'), ('4th', 'Fourth-Year'), ('Other', 'Other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
