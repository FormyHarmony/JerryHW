# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_twxt',
            new_name='question_text',
        ),
    ]
