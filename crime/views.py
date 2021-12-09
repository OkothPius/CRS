from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
from django.views import generic
from django.db.models import Q
from .render import Render
from django.contrib import messages
from crime.models import Log, Category
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
                    ListView,
                    CreateView,
                    UpdateView,
                    DetailView,
                    DeleteView
                    )
from .filters import LogFilter

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

class LogListView(ListView):
    model = Log
    template_name = 'crime/index.html' #<app/<model>_<viewtype>.html
    context_object_name = 'logs'
    ordering = ['-date_posted']
    paginate_by = 20

class UserLogListView(ListView):
    model = Log
    # my_filter = LogFilter()
    template_name = 'crime/user_logs.html' #<app/<model>_<viewtype>.html
    context_object_name = 'logs'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        myFilter = LogFilter(self.request.GET, queryset)
        return myFilter.qs

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Log.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        myFilter = LogFilter(self.request.GET, queryset)
        context["myFilter"] = myFilter
        return context

    # def get(self, request, *args, **kwargs):
    #     self.object_list = self.get_queryset()
    #     context = self.get_context_data(**kwargs)
    #     logs = Log.objects.all()
    #     myFilter = LogFilter(request.GET, queryset=logs)
    #     logs = myFilter.qs
    #
    #     context['myFilter'] = myFilter
    #     return render(request, self.template_name, context)
        # return context

class LogDetailView(DetailView):
    model = Log

class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ['case', 'details', 'location', 'type', 'num_reported', 'attach_file']

    #Uses the current user as the author of posts created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LogUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    success_message ='Your Post have been Updated!'
    model = Log
    fields = ['case', 'details', 'location', 'type', 'num_reported', 'attach_file']

    #Uses the current user as the author of posts created
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        log = self.get_object()
        if self.request.user == log.author:
            return True

class LogDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    success_message ='Your Post have been Deleted!'
    model = Log
    success_url = '/'

    def test_func(self):
        log = self.get_object()
        if self.request.user == log.author:
            return True

class PdfView(generic.TemplateView):

    def get(self, request):
        crimes = Log.objects.all()
        today = timezone.now()

        params = {
            'today': today,
            'crimes': crimes,
            'request': request
        }

        return Render.render('crime/pdf.html', params)

#Search view
class SearchView(generic.TemplateView):
    template_name = 'crime/search.html'
    models = Log

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
           queryset = Log.objects.filter(case__icontains=query)
        else:
            queryset = Log.objects.all()
        return queryset

    #
    #     return Log.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     kw = self.request.GET.get('keyword')
    #     logs = Log.objects.filter(Q(location__icontains=kw) | Q(author__icontains=kw))
    #     print('logs')
    #     context['logs'] = logs
    #     return context
