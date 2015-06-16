from django.db import models

from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Change(models.Model):
	datetime = models.DateTimeField('date change')
	user = models.ForeignKey(AUTH_USER_MODEL)
	description = models.CharField(max_length=200)
