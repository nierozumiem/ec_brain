# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serwis', '0005_auto_20160903_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urzadzenie',
            name='multi',
            field=models.IntegerField(choices=[(1, 'TAK'), (0, 'NIE')]),
        ),
        migrations.AlterField(
            model_name='urzadzenie',
            name='strategiczny',
            field=models.IntegerField(choices=[(1, 'TAK'), (0, 'NIE')]),
        ),
    ]