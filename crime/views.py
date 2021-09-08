from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib import messages
from crime.models import Log, Category
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	return render(request, 'crime/home.html')

def log(request):
	context = {
		'logs': Log.objects.all()
	}
	return render(request, 'crime/log.html', context)

def issue(request):
	context = {
		'issues': Log.objects.all()
	}
	return render(request, 'crime/issues.html', context)

def police_post(request):
	return render(request, 'crime/police_post.html')

def about(request):
 return render(request, 'crime/about.html')

def pie_chart(request):
	labels = []
	data = []

	queryset = Log.objects.order_by('-num_reported')[:5]
	for log in queryset:
		labels.append(log.case)
		data.append(log.num_reported)

	return render(request, 'crime/pie-chart.html', {
		'labels': labels,
		'data': data,
	})

def report_chart(request):
	labels = []
	data = []

	queryset = Log.objects.values('type__name').annotate(type_num_reported=Sum\
								('num_reported')).order_by('-type_num_reported')
	for entry in queryset:
		labels.append(entry['type__name'])
		data.append(entry['type_num_reported'])

	return JsonResponse(data={
		'labels':labels,
		'data': data,
	})


class PostListView(ListView):
    model = Log
    template_name = 'crime/log.html' #<app/<model>_<viewtype>.html
    context_object_name = 'logs'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ['case', 'details', 'location', 'type', 'num_reported']

    #Uses the current user as the author of posts created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
