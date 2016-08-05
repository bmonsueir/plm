# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('attribute', models.CharField(max_length=255)),
                ('updatedBy', models.CharField(max_length=255)),
                ('references', models.CharField(max_length=255)),
                ('permissions', models.CharField(max_length=255)),
                ('updatedAt', models.CharField(max_length=255)),
            ],
        ),
    ]
