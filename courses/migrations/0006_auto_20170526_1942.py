# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-26 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20170526_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='assisttant',
            new_name='assistant',
        ),
    ]
