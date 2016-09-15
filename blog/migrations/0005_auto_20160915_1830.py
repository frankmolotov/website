# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160829_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='registration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]