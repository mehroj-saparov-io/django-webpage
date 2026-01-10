# core/models.py
from django.db import models
from urllib.parse import urlparse, parse_qs

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_video_id(self):
        parsed = urlparse(self.youtube_url)
        if 'v' in parse_qs(parsed.query):
            return parse_qs(parsed.query)['v'][0]
        return ''

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']