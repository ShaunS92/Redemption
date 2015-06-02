# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_auto_20150528_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_related',
            field=models.TextField(default=b'Empty', null=True),
        ),
    ]
