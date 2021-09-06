from django.urls import path
from .views import PostListView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='logs'),
    path('home/', views.home, name='home'),
    path('log/new/', PostCreateView.as_view(), name='log-create'),
    path('about/', views.about, name='about'),
]
