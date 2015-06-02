# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0016_auto_20150530_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 16, 40, 38, 913523, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
