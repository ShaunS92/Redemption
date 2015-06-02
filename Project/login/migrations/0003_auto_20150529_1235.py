# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userprofile_profil_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profil_pic',
            field=models.TextField(default=b'home/ronan/Redemption/Project/none.jpg'),
        ),
    ]
