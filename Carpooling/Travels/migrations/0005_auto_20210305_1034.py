# Generated by Django 3.1.7 on 2021-03-05 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20210305_1027'),
        ('Travels', '0004_auto_20210305_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='Passenger1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Passenger1_type', to='User.user'),
        ),
        migrations.AlterField(
            model_name='travels',
            name='Passenger2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Passenger2_type', to='User.user'),
        ),
    ]