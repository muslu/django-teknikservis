# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servisformu', '0002_auto_20160114_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteriler',
            name='Kodu',
            field=models.CharField(default='87473836', max_length=8, verbose_name='M\xfc\u015fteri Kodu'),
        ),
        migrations.AlterField(
            model_name='servisform',
            name='FormNo',
            field=models.CharField(default='39584910', max_length=8, verbose_name='Form No'),
        ),
    ]
