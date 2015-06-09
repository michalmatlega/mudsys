from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class Item(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(max_length=800, default='Description')
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)


    def progress_(self):
        return "<div style='width: 100px; border: 1px solid #ccc;'>" + \
               "<div style='height: 4px; width: %dpx; background: #555; '></div></div>" % self.progress
    progress_.allow_tags = True


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created", "desc", "priority", "difficulty", "done", "progress"]
    search_fields = ["priority"]
