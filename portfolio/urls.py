from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

import jobs.views

from .sitemap import JobSitemap, StaticSitemap

sitemaps = {
    'jobs': JobSitemap,
    'static': StaticSitemap,
}

urlpatterns = [

    # admin
    path('gc_admin/', admin.site.urls),

    # apps
    path('contact/', include('contact.urls')),
    path('portfolio/', include('jobs.urls')),
    path('', jobs.views.home, name='home'),

    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
