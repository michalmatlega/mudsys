from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from fileman.models import Document
from fileman.forms import DocumentForm

from history.models import Change

import datetime

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            descstr = "Dodano plik " + request.FILES['docfile'].name
            change = Change()
            change.datetime = datetime.datetime.now()
            change.description = descstr
            change.user = request.user
            change.save()

            return HttpResponseRedirect('/files/')

    else:
        form = DocumentForm()

    documents = Document.objects.all()

    return render_to_response(
        'fileman/list.html',
        {'documents': documents, 'form':form},
        context_instance=RequestContext(request)
    )

def delete(request, id):
    Document.objects.filter(id=id).delete()
