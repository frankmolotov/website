# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160915_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='count_of_users',
            field=models.CharField(default='257329', max_length=100, null=True),
        ),
    ]