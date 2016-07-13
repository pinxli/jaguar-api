# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankingInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('account', models.CharField(blank=True, max_length=100, null=True)),
                ('memo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'bank_bankinginfo',
            },
        ),
    ]
