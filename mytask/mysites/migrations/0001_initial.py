# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Site Name')),
            ],
        ),
        migrations.CreateModel(
            name='MySiteValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='A value')),
                ('b_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='B value')),
                ('date', models.DateField(verbose_name='When it is')),
                ('mysite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysites.MySite')),
            ],
        ),
    ]
