# core/urls.py
from django.urls import path
from .views import AboutView, LectureListView, ProjectListView, BlogListView, BlogDetailView, ContactView

urlpatterns = [
    path('', AboutView.as_view(), name='home'),          # ← root sahifa (about)
    path('about/', AboutView.as_view(), name='about'),
    path('lectures/', LectureListView.as_view(), name='lectures'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]