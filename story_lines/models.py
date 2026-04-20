from django.db import models
from django.utils import timezone, User

# Create your models here.


class StoryLine(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='story_lines')
    excerpt_name = models.CharField(max_length=200, unique=True)
    story_date = models.DateTimeField(default=timezone.now)
    story_summary = models.CharField(max_length=200)
    story_excerpt = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    excerpt_image = models.ImageField(upload_to='story_excerpts/')
