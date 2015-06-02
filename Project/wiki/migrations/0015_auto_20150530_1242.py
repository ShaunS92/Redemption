# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_auto_20150530_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_introduction',
            new_name='article_content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_rating',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_soil',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_sunlight',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_watering',
        ),
        migrations.AlterField(
            model_name='article_content_history',
            name='article_content_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 42, 24, 977039, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
