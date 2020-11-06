from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=4)),
                ('catalog_number', models.CharField(max_length=4)),
                ('class_title', models.CharField(max_length=100)),
            ],
        ),
    ]
