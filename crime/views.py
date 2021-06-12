from django.shortcuts import render
from .models import Log
from django.contrib.auth.models import User

def home(request):
	text = 'Hey There'
	context = {
	'context_text':text
	}
	return render(request, 'crime/home.html', context)

def log(request):
	context = {
		'logs': Log.objects.all()
	}
	return render(request, 'crime/log.html', context)
