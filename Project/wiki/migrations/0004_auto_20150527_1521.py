# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20150527_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_introduction',
            field=models.CharField(default=b'New Article', max_length=b'140', null=True),
        ),
    ]
