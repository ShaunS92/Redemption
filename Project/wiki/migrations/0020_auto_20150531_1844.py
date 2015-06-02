# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0019_auto_20150531_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.TextField(default=b'New Article', max_length=b'140', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.TextField(default=b'New Article', max_length=b'140'),
        ),
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 31, 18, 44, 40, 547926, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
