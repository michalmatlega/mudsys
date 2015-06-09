from django.contrib import admin
from taskman.models import *

admin.site.register(Item, ItemAdmin)
