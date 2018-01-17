# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
    ]