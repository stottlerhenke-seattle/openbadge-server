# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbadge', '0027_datafile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datafile',
            name='hub',
        ),
        migrations.DeleteModel(
            name='DataFile',
        ),
    ]