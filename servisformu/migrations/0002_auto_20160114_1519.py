# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servisformu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteriler',
            name='Kodu',
            field=models.CharField(default='77514188', max_length=8, verbose_name='M\xfc\u015fteri Kodu'),
        ),
        migrations.AlterField(
            model_name='servisform',
            name='FormNo',
            field=models.CharField(default='49942436', max_length=8, verbose_name='Form No'),
        ),
    ]
