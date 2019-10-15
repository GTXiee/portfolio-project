from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe

from taggit.managers import TaggableManager


class Job(models.Model):
    title = models.CharField(max_length=200, default='change me')
    url_slug = models.SlugField(max_length=50)
    link_to_project = models.URLField(max_length=200, blank=True)
    summary = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    technologies = ArrayField(
        models.CharField(
            max_length=50,
        ),
        null=True
    )
    tags = TaggableManager(blank=True)
    date_created = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.url_slug)])


class JobImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('TN', 'Thumbnail'),
        ('DS', 'Display'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=IMAGE_TYPE_CHOICES,
        default='DS',
    )
    image = models.ImageField(upload_to='images/')

    order = models.IntegerField(
        choices=[(i, i) for i in range(4)],
    )

    def __str__(self):
        return self.image.name
