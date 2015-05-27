# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_remove_article_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_introduction',
            field=models.CharField(default=b'New Article', max_length=b'140'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_rating',
            field=models.TextField(default=b'No rating yet'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_soil',
            field=models.TextField(default=b'No information on soil added yet! Be the fisrt to post something!'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_sunlight',
            field=models.TextField(default=b'No information on sunlight added yet! Be the fisrt to post something!'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_watering',
            field=models.TextField(default=b'No information on watering added yet! Be the fisrt to post something!'),
        ),
    ]
