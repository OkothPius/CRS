from django.shortcuts import render

def home(request):
	text = 'Hey There'
	context = {
	'context_text':text
	}
	return render(request, 'crime/home.html', context)
