from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
from django.utils import timezone
from django.utils.safestring import mark_safe

from taggit.managers import TaggableManager


class Job(models.Model):
    title = models.CharField(max_length=200, default='change me')
    url_slug = models.SlugField(max_length=50, unique=True)
    link_to_project = models.URLField(max_length=200, blank=True)
    summary = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    # technologies = ArrayField(
    #     models.CharField(
    #         max_length=50,
    #     ),
    #     null=True
    # )
    tags = TaggableManager(blank=True)
    date_created = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.url_slug)])


class JobImage(models.Model):
    job_linked = models.ForeignKey(Job, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    is_thumbnail = models.BooleanField(default=None, null=True, blank=True)
    order = models.IntegerField()

    class Meta:
        unique_together = (('job_linked', 'order'), ('job_linked', 'is_thumbnail'))

    def save(self, *args, **kwargs):
        if self.is_thumbnail is False:
            self.is_thumbnail = None
        super(JobImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.name
