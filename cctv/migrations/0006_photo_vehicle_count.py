# Generated by Django 3.0.3 on 2020-03-07 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0005_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='vehicle_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
