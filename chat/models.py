from django.db import models

from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ChatRoom(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Message(models.Model):
	chatRoom = models.ForeignKey(ChatRoom)
	user = models.ForeignKey(AUTH_USER_MODEL)
	datetime = models.DateTimeField('date published')
	content = models.CharField(max_length=200)


