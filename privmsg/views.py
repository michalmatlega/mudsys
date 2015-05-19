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
	msg.toUser = User.objects.get(username = request.POST['touser'])
	msg.subject = request.POST['subject']
	msg.content = request.POST['content']
	msg.datetime = datetime.datetime.now()
	msg.save()
	return render(request,"pm/outbox.html")

def readMsg(request,msg_id):
	msg = PMessage.objects.get(id = msg_id)
	if msg.read == False and msg.toUser == request.user:
		msg.read = True
		msg.readdatetime = datetime.datetime.now()
		msg.save()

def show(request,msg_id):
	readMsg(request,msg_id)

	msg = PMessage.objects.get(id = msg_id)

	context = {
		'msg': msg,
	}
	return render(request,'pm/show.html', context)

def reply(request,msg_id):
	msgre = PMessage.objects.get(id = msg_id)
	
	msgtosend = PMessage()
	
	msgtosend.fromUser = request.user
	msgtosend.toUser = msgre.fromUser
	msgtosend.content = request.POST['content']
	msgtosend.datetime = datetime.datetime.now()
	msgtosend.subject = "RE: " + msgre.subject

	msgtosend.save()

	return render(request,"pm/outbox.html")