# Generated by Django 3.1.7 on 2021-03-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travels', '0002_auto_20210304_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]