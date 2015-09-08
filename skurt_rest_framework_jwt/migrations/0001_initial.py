# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParseUserProxy',
            fields=[
                ('objectId', models.CharField(max_length=16, unique=True, serialize=False, primary_key=True)),
            ],
        ),
    ]
