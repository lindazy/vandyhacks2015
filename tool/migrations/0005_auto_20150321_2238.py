# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tool.models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0004_item_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='paper',
            name='mesh',
            field=tool.models.ListField(default=[]),
            preserve_default=True,
        ),
    ]
