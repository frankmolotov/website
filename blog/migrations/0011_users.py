# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160915_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_of_users', models.CharField(default='257329', max_length=100, null=True)),
                ('capital', models.CharField(default='1452900', max_length=100, null=True)),
            ],
        ),
    ]
