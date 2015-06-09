from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse


class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "priority", "difficulty", "done"]
    search_fields = ["name"]
