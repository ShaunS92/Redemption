# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150601_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rating',
        ),
    ]
