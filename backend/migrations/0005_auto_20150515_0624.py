# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20150514_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='color',
            field=models.CharField(blank=True, max_length=50, default='steelblue'),
        ),
        migrations.AlterField(
            model_name='run',
            name='name',
            field=models.CharField(blank=True, max_length=255, default=''),
        ),
    ]
