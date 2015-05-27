# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20150515_0624'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('owner', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='run',
            unique_together=set([('project', 'slug')]),
        ),
    ]
