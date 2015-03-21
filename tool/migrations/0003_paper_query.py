# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='query',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
