# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_article_introduction_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_introduction_history',
            field=models.TextField(default=b'Empty', null=True),
        ),
    ]
