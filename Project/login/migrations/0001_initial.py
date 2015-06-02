# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthdate', models.DateField(null=True)),
                ('rating', models.IntegerField(default=5)),
                ('description', models.TextField(default=b'')),
                ('ip_address', models.TextField(default=b'0.0.0.0')),
            ],
        ),
    ]
