# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_register_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
    ]
