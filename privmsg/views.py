from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from privmsg.models import PMessage
from django.contrib.auth.models import User

import datetime

def inbox(request):
	inbox_list = PMessage.objects.filter(toUser = request.user)
	context = {
		'inbox_list': inbox_list,
	}
	return render(request,'pm/inbox.html', context)

def outbox(request):
	outbox_list = PMessage.objects.filter(fromUser = request.user)
	context = {
		'outbox_list': outbox_list,
	}
	return render(request,'pm/outbox.html', context)

def send(request):
	msg = PMessage()
	msg.fromUser = request.user
	msg.toUser = request.POST['touser']
	msg.subject = request.POST['subject']
	msg.content = request.POST['content']
	msg.datetime = datetime.datetime.now()
	msg.save()
	return render(request,"pm/outbox.html")

def show(request,msg_id):
	return render(request,'pm/')
