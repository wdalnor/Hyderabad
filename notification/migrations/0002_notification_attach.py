# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
