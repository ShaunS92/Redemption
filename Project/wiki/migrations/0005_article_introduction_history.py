# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20150527_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Introduction_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_introduction_history', models.TextField(default=b'Empty')),
                ('article_related', models.ForeignKey(to='wiki.Article')),
            ],
        ),
    ]
