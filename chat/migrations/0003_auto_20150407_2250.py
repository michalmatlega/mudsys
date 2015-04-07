# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
    ]
