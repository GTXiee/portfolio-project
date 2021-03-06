from django.contrib import admin

from .models import Job, JobImage


# Defines inline JobImage object
class JobImageInline(admin.TabularInline):
    model = JobImage
    fields = ('image', 'is_thumbnail', 'order')
    extra = 0


# Allows images to be shown within Job admin
class JobAdmin(admin.ModelAdmin):
    inlines = [
        JobImageInline,
    ]
    prepopulated_fields = {'url_slug': ('title',)}



admin.site.register(Job, JobAdmin)
