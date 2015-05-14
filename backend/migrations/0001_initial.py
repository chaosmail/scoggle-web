# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import backend.helpers.fields
import uuid
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('project_id', models.UUIDField(unique=True, editable=False, default=uuid.uuid4)),
                ('created_at', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('edited_at', backend.helpers.fields.AutoDateTimeField(editable=False, default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='')),
                ('url', models.URLField(default='')),
                ('name', models.CharField(max_length=255, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('result_id', models.UUIDField(unique=True, editable=False, default=uuid.uuid4)),
                ('created_at', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('is_valid', models.BooleanField(default=True)),
                ('score', models.DecimalField(max_digits=20, default=0.0, decimal_places=12)),
                ('duration', models.DecimalField(blank=True, max_digits=14, default=0.0, decimal_places=6)),
                ('params', jsonfield.fields.JSONField(blank=True, default={})),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('run_id', models.UUIDField(unique=True, editable=False, default=uuid.uuid4)),
                ('name', models.CharField(max_length=255, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('edited_at', backend.helpers.fields.AutoDateTimeField(editable=False, default=django.utils.timezone.now)),
                ('project', models.ForeignKey(to='backend.Project')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='run',
            field=models.ForeignKey(to='backend.Run'),
        ),
    ]
