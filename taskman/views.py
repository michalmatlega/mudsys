from taskman.models import *
from django.shortcuts import render_to_response

def index(request):
    item = Item.objects.order_by('priority')  #[:5] #all()

    return render_to_response('tasks/index.html', {'item': item})
