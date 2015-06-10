# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField(default='Description', max_length=800)),
                ('priority', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('progress', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
