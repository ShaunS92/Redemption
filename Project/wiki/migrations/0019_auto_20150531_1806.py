# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0018_auto_20150531_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_content_history',
            name='article_author',
            field=models.TextField(default=b'Empty', null=True),
        ),
        migrations.AddField(
            model_name='article_content_history',
            name='article_author_id',
            field=models.TextField(default=b'Empty', null=True),
        ),
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 31, 18, 6, 7, 59662, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
