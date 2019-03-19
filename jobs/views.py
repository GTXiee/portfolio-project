from django.shortcuts import render, get_object_or_404

from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'latest_jobs': jobs})


def projects(request):
    jobs = Job.objects.all()[:3]
    return render(request, 'jobs/projects.html', {'latest_jobs': jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job})
