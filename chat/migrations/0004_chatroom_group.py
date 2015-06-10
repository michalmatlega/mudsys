# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('chat', '0003_auto_20150407_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='group',
            field=models.ForeignKey(to='auth.Group', default=0),
            preserve_default=False,
        ),
    ]
