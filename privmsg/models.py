from django.db import models

# Create your models here.

from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class PMessage(models.Model):
	fromUser = models.ForeignKey(AUTH_USER_MODEL)
	toUser = models.ForeignKey(AUTH_USER_MODEL)
	subject = models.CharField(max_length=50)
	read = models.BooleanField(default = false)
	readdatetime = models.DateTimeField('date read', null = true)
	datetime = models.DateTimeField('date sent')
	content = models.CharField(max_length=200)
	def __str__(self):
		return self.content

