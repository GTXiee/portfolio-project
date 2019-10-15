from django.contrib import admin

from .models import Job, JobImage


# Defines inline JobImage object
class JobImageInline(admin.TabularInline):
    model = JobImage
    fields = ('image', 'type', 'order')
    extra = 0


# Allows images to be shown within Job admin
class JobAdmin(admin.ModelAdmin):
    inlines = [
        JobImageInline,
    ]


admin.site.register(Job, JobAdmin)
