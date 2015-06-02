# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150529_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profil_pic',
            new_name='profile_pic',
        ),
    ]
