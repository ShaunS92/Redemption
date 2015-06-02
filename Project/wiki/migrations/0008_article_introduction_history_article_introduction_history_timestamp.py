# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20150528_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_introduction_history',
            name='article_introduction_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 18, 55, 38, 223964, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
