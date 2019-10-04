from django.shortcuts import render, get_object_or_404

from .models import Job


def home(request):
    jobs = Job.objects.order_by('-date_created')
    return render(request, 'jobs/home.html', {'latest_jobs': jobs})


def projects(request):
    jobs = Job.objects.order_by('-date_created')[:3]
    return render(request, 'jobs/projects.html', {'latest_jobs': jobs})


def job_detail(request, slug):
    job = get_object_or_404(Job, url_slug=slug)
    if job.title == "Keyword Wrapper":
        template = 'jobs/keyword-wrapper.html'
    else:
        template = 'jobs/detail.html'
    return render(request, template, {'job': job})
