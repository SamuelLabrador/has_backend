# Generated by Django 2.2.9 on 2020-02-03 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CCTVImage',
            new_name='Image',
        ),
    ]
