from django.shortcuts import render, get_object_or_404

from .models import Job, JobImage


def home(request):
    jobs = Job.objects.order_by('-date_created')[:3]
    job_data = []
    for job in jobs:
        # Will throw error if more than thumbnail image
        job_data.append({
            'job': job,
            'image': JobImage.objects.get(job=job.id, type='TN').image
        })
    return render(request, 'jobs/home.html', {'job_data': job_data})


def projects(request):
    jobs = Job.objects.order_by('-date_created')[:3]
    job_data = []
    for job in jobs:
        # Will throw error if more than thumbnail image
        job_data.append({
            'job': job,
            'image': JobImage.objects.get(job=job.id, type='TN').image
        })
    return render(request, 'jobs/projects.html', {'job_data': job_data})


def job_detail(request, slug):
    job = get_object_or_404(Job, url_slug=slug)
    images = JobImage.objects.filter(
        job=job.id
    ).filter(
        type='DS'
    ).order_by(
        'order'
    )

    if job.title == "Keyword Wrapper":
        template = 'jobs/keyword-wrapper.html'
    else:
        template = 'jobs/detail.html'

    context = {
        'job': job,
        'images': images,
    }
    return render(request, template, context)
