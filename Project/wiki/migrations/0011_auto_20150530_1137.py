# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0010_auto_20150530_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Rating_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_rating_history', models.TextField(default=b'Empty', null=True)),
                ('article_related', models.TextField(default=b'Empty', null=True)),
                ('article_rating_history_timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 30, 11, 37, 40, 62940, tzinfo=utc), verbose_name=b'Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Soil_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_soil_history', models.TextField(default=b'Empty', null=True)),
                ('article_related', models.TextField(default=b'Empty', null=True)),
                ('article_soil_history_timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 30, 11, 37, 40, 63440, tzinfo=utc), verbose_name=b'Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Sunlight_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_sunlight_history', models.TextField(default=b'Empty', null=True)),
                ('article_related', models.TextField(default=b'Empty', null=True)),
                ('article_sunlight_history_timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 30, 11, 37, 40, 63886, tzinfo=utc), verbose_name=b'Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Watering_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_watering_history', models.TextField(default=b'Empty', null=True)),
                ('article_related', models.TextField(default=b'Empty', null=True)),
                ('article_watering_history_timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 30, 11, 37, 40, 64370, tzinfo=utc), verbose_name=b'Timestamp')),
            ],
        ),
        migrations.AlterField(
            model_name='article_introduction_history',
            name='article_introduction_history_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 11, 37, 40, 62480, tzinfo=utc), verbose_name=b'Timestamp'),
        ),
    ]
