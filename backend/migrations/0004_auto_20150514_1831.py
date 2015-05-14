# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_run_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='color',
            field=models.CharField(max_length=50, default='steelblue'),
        ),
        migrations.AlterField(
            model_name='run',
            name='project',
            field=models.ForeignKey(to='backend.Project', related_name='runs'),
        ),
        migrations.AlterField(
            model_name='score',
            name='run',
            field=models.ForeignKey(to='backend.Run', related_name='scores'),
        ),
    ]
