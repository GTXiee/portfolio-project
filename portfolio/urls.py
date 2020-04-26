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
    path('gc-admin/', admin.site.urls),

    # apps
    path('', include('pages.urls')),
    path('contact/', include('contact.urls')),
    path('portfolio/', include('jobs.urls')),

    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]
if not settings.USE_SFTP:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
