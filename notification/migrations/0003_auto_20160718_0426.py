# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-18 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='notifications_files/%Y.%m.%d'),
        ),
    ]
