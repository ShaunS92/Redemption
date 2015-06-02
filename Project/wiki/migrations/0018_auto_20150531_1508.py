# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_auto_20150530_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 31, 15, 8, 57, 417959, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
