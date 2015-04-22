from django.db import models

# Create your models here.

class Change(models.Model):
	datetime = models.DateTimeField('date change')
	description = models.CharField(max_length=200)
