# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_userprofile_user_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_auth',
            field=models.IntegerField(default=1),
        ),
    ]
