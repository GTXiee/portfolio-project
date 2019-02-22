from django.db import models

from taggit.managers import TaggableManager


class Job(models.Model):
    title = models.CharField(max_length=200, default='change me')
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=200)
    tags = TaggableManager()


def __str__(self):
    return self.title
