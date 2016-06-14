# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of Study')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(verbose_name='Version')),
                ('created_by', models.CharField(blank=True, max_length=255, verbose_name='Created by')),
                ('save_date', models.DateTimeField(auto_now_add=True)),
                ('json', jsonfield.fields.JSONField(verbose_name='Enter a valid Treefile JSON:')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to='trees.Study')),
            ],
        ),
    ]