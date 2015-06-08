from django.contrib import admin
from django.db import models


class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.datetime)


class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "priority", "difficulty", "done"]
    search_fields = ["name"]


class ItemInLine(admin.TabularInline):
    model = Item


class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInLine]


admin.site.register(Item, ItemAdmin)
admin.site.register(DateTime, DateAdmin)
