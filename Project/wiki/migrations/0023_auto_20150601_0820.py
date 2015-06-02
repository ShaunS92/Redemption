# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0022_auto_20150601_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 8, 20, 59, 811225, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(default=b'New Category', max_length=b'140'),
        ),
    ]
