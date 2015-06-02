# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0021_auto_20150601_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 8, 19, 38, 747062, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
