# core/admin.py
from django.contrib import admin
from .models import Lecture, Project, Post

admin.site.register(Lecture)
admin.site.register(Project)
admin.site.register(Post)