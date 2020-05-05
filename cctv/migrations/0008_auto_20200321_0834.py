# Generated by Django 3.0.3 on 2020-03-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0007_vehicle_labels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='labels',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='probability',
            field=models.FloatField(blank=True, null=True),
        ),
    ]