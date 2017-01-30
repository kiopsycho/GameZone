# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 19:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_game_image_bar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_review',
            name='score',
        ),
        migrations.AddField(
            model_name='game_review',
            name='gameplay_score',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='game_review',
            name='graphics_score',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='game_review',
            name='story_score',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]