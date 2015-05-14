# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150512_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
