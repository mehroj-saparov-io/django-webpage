# seed_data.py
# Run this script after migrations: python manage.py shell < seed_data.py
from core.models import Lecture, Project, Post

# Sample Lectures (10 total, 3 categories: 5 Database, 3 Django, 2 Marketing)
lectures = [
    ('Database Basics 1', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Database'),
    ('Database Basics 2', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Database'),
    ('Database Basics 3', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Database'),
    ('Database Basics 4', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Database'),
    ('Database Basics 5', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Database'),
    ('Django Intro', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Django'),
    ('Django Models', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Django'),
    ('Django Views', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Django'),
    ('Marketing 101', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Marketing'),
    ('Marketing Strategies', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Marketing'),
]

for title, url, cat in lectures:
    Lecture.objects.get_or_create(title=title, defaults={'youtube_url': url, 'category': cat})

# Sample Projects (3)
projects = [
    ('Project 1', 'Sample description for project 1.', 'Django, Python', 'https://github.com/project1'),
    ('Project 2', 'Sample description for project 2.', 'SQL, REST', 'https://github.com/project2'),
    ('Project 3', 'Sample description for project 3.', 'DevOps, Cloud', 'https://github.com/project3'),
]

for title, desc, tech, link in projects:
    Project.objects.get_or_create(title=title, defaults={'description': desc, 'tech_stack': tech, 'github_link': link})
    # Note: Images to be uploaded via admin

# Sample Blog Posts (2, with Markdown)
posts = [
    ('First Post', '# Hello\nThis is a **sample** post with Markdown.'),
    ('Second Post', '## Subtitle\n- List item\n- Another item'),
]

for title, content in posts:
    Post.objects.get_or_create(title=title, defaults={'content': content})