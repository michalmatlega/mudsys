from django.contrib import admin
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "docfile"]
    search_fields = ["docfile"]