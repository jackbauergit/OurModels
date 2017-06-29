# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('discribtion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('passwd', models.CharField(max_length=32)),
                ('login', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermissin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('Permission_id', models.IntegerField()),
                ('delete', models.CharField(max_length=32)),
            ],
        ),
    ]