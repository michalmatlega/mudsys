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
            name='PMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(max_length=50)),
                ('read', models.BooleanField(default=False)),
                ('readdatetime', models.DateTimeField(null=True, verbose_name='date read')),
                ('datetime', models.DateTimeField(verbose_name='date sent')),
                ('content', models.CharField(max_length=200)),
                ('fromUser', models.ForeignKey(related_name='requests_from', to=settings.AUTH_USER_MODEL)),
                ('toUser', models.ForeignKey(related_name='requests_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
