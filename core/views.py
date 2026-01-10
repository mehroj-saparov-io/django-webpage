# core/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Count
from .models import Lecture, Project, Post
import markdown

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class LectureListView(ListView):
    model = Lecture
    template_name = 'lectures.html'
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        if category and category != 'ALL':
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = Lecture.objects.count()
        categories = Lecture.objects.values('category').annotate(count=Count('category')).order_by('-count')
        top_categories = categories[:3]
        other_categories = categories[3:]
        context['total_lectures'] = total
        context['categories'] = categories
        context['top_categories'] = top_categories
        context['other_categories'] = other_categories
        context['current_category'] = self.request.GET.get('category', 'ALL')
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'

class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_html'] = markdown.markdown(self.object.content, extensions=['fenced_code', 'codehilite'])
        return context