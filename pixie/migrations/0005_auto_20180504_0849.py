# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-04 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixie', '0004_auto_20180504_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pixie.Location'),
        ),
    ]
