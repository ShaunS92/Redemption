# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profil_pic',
            field=models.ImageField(default=b'none.jpeg', upload_to=b'/home/ronan/Redemption/Project/login/images/'),
        ),
    ]
