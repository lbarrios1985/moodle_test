# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_curse', models.IntegerField()),
                ('enum', models.CharField(max_length=1000)),
                ('feedback', models.TextField()),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
