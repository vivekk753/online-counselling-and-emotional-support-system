# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-06 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselor', '0002_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.PositiveIntegerField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counselor.message')),
            ],
        ),
    ]
