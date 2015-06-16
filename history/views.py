from django.shortcuts import render

from history.models import Change

def index(request):
	changes = Change.objects.order_by('-datetime')

	context = {
		'changes': changes,
	}
	return render(request,'history/index.html', context)
