# Generated by Django 3.1.7 on 2021-03-23 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Travels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='createdOn',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
