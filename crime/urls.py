from django.urls import path
from .views import (
        LogListView,
        LogCreateView,
        LogUpdateView,
        LogDeleteView,
        UserLogListView,
        LogDetailView,
        PdfView
        )
from . import views

urlpatterns = [
    path('', LogListView.as_view(), name='log-home'),
    path('log/<str:username>', UserLogListView.as_view(), name='user-logs'),
    path('visuals/', views.home, name='home'),
    path('log/new/', LogCreateView.as_view(), name='log-create'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log-detail'),
    path('log/<int:pk>/update/', LogUpdateView.as_view(), name='log-update'),
    path('log/<int:pk>/delete/', LogDeleteView.as_view(), name='log-delete'),
    path('issues/', views.issue, name='issue'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('report-chart/', views.report_chart, name='report-chart'),
    path('police-post/', views.police_post, name='police-post'),
    path('about/', views.about, name='about'),
    path('download/', PdfView.as_view(), name='download'),
]
