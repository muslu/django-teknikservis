# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servisformu', '0007_auto_20160115_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteriler',
            name='Kodu',
            field=models.CharField(default='82157338', max_length=8, verbose_name='M\xfc\u015fteri Kodu'),
        ),
        migrations.AlterField(
            model_name='servisform',
            name='FormNo',
            field=models.CharField(default='90197119', max_length=8, verbose_name='Form No'),
        ),
    ]
