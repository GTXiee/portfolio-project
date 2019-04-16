from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from taggit.managers import TaggableManager


class Job(models.Model):
    title = models.CharField(max_length=200, default='change me')
    slug = models.SlugField(max_length=50)
    url = models.URLField(max_length=200, blank=True)
    portfolio_image = models.ImageField(upload_to='images/', blank=True)
    display_image = models.ImageField(upload_to='images/', blank=True)
    summary = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.slug)])

