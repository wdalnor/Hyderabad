# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_likes_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes_num',
        ),
        migrations.AddField(
            model_name='likes',
            name='likes_num',
            field=models.IntegerField(default=0),
        ),
    ]
