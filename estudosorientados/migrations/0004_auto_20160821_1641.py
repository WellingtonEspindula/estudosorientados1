# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudosorientados', '0003_auto_20160821_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='numero_turma',
            field=models.IntegerField(),
        ),
    ]
