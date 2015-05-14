# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('score_id', models.UUIDField(unique=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_valid', models.BooleanField(default=True)),
                ('score', models.DecimalField(default=0.0, decimal_places=12, max_digits=20)),
                ('duration', models.DecimalField(default=0.0, max_digits=14, decimal_places=6, blank=True)),
                ('params', jsonfield.fields.JSONField(default={}, blank=True)),
                ('run', models.ForeignKey(to='backend.Run')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='run',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
