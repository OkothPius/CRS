from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView
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

def about(request):
 return render(request, 'crime/about.html')


class PostListView(ListView):
    model = Log
    template_name = 'crime/log.html' #<app/<model>_<viewtype>.html
    context_object_name = 'logs'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ['case', 'details', 'location']

    #Uses the current user as the author of posts created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
