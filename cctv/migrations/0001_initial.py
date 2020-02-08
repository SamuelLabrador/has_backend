# Generated by Django 2.2.1 on 2020-01-16 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.IntegerField()),
                ('location_name', models.CharField(blank=True, max_length=255, null=True)),
                ('nearby_place', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('elevation', models.IntegerField()),
                ('direction', models.CharField(blank=True, max_length=255, null=True)),
                ('county', models.CharField(blank=True, max_length=255, null=True)),
                ('route', models.CharField(blank=True, max_length=255, null=True)),
                ('route_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('postmile_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('postmile', models.CharField(blank=True, max_length=255, null=True)),
                ('alignment', models.CharField(blank=True, max_length=255, null=True)),
                ('milepost', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('stream_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CCTVImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cctv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cctv.CCTV')),
            ],
        ),
    ]