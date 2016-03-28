# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterData', '0004_tweet_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='polarity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='subjectivity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
