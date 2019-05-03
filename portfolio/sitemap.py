from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from jobs.models import Job


class JobSitemap(Sitemap):

    def items(self):
        return Job.objects.all()


class StaticSitemap(Sitemap):

    def items(self):
        return ['home', 'contact', 'projects']

    def location(self, item):
        return reverse(item)
