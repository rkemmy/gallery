# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-04 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='pixie.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pixie.Location'),
        ),
    ]
