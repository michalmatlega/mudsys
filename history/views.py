from django.shortcuts import render

def index(request):
	changes = Change.objects.order_by('-date')

	context = {
		'changes': changes,
	}
	return render(request,'history/index.html', context)
