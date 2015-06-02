# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0013_auto_20150530_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Content_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_content_history', models.TextField(default=b'Empty', null=True)),
                ('article_related', models.TextField(default=b'Empty', null=True)),
                ('article_content_history_timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 39, 18, 428540, tzinfo=utc), verbose_name=b'Timestamp')),
            ],
        ),
        migrations.DeleteModel(
            name='Article_Introduction_History',
        ),
    ]
