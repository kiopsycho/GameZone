# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170122_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='game',
            name='short_description',
            field=models.CharField(max_length=450, null=True),
        ),
    ]
