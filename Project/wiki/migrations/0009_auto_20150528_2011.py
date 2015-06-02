# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_article_introduction_history_article_introduction_history_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_rating',
            field=models.TextField(default=b'No rating yet', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_soil',
            field=models.TextField(default=b'No information on soil added yet! Be the fisrt to post something!', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_sunlight',
            field=models.TextField(default=b'No information on sunlight added yet! Be the fisrt to post something!', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_watering',
            field=models.TextField(default=b'No information on watering added yet! Be the fisrt to post something!', null=True),
        ),
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_introduction_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 20, 11, 0, 712096, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
