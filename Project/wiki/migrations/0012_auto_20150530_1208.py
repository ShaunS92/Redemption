# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0011_auto_20150530_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_introduction_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 8, 23, 693532, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
        migrations.AlterField(
            model_name='article_rating_history',
            name='article_rating_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 8, 23, 694048, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
        migrations.AlterField(
            model_name='article_soil_history',
            name='article_soil_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 8, 23, 694528, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
        migrations.AlterField(
            model_name='article_sunlight_history',
            name='article_sunlight_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 8, 23, 695050, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
        migrations.AlterField(
            model_name='article_watering_history',
            name='article_watering_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 8, 23, 695535, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
