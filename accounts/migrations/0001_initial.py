# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-10 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('location', models.CharField(default='', max_length=140)),
                ('gender', models.CharField(choices=[('undefined', 'UNDEFINED'), ('female', 'FEMALE'), ('male', 'MALE')], default='undefined', max_length=6)),
                ('bio', models.CharField(default='', max_length=240)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
