from django.urls import path
from .views import PostListView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='logs'),
    path('visuals/', views.home, name='home'),
    path('log/new/', PostCreateView.as_view(), name='log-create'),
    path('issues/', views.issue, name='issue'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('report-chart/', views.report_chart, name='report-chart'),
    path('about/', views.about, name='about'),
]
