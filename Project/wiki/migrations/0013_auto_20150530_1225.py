# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_auto_20150530_1208'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article_Rating_History',
        ),
        migrations.DeleteModel(
            name='Article_Soil_History',
        ),
        migrations.DeleteModel(
            name='Article_Sunlight_History',
        ),
        migrations.DeleteModel(
            name='Article_Watering_History',
        ),
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_introduction_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 25, 9, 198268, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
