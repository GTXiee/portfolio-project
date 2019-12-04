from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
import logging

from .models import Job, JobImage

logger = logging.getLogger(__name__)

# def portfolio_page(request):
#     jobs = Job.objects.order_by('-date_created')[:3]
#     job_data = []
#     for job in jobs:
#         # Will throw error if more than thumbnail image
#         job_data.append({
#             'job': job,
#             'image': JobImage.objects.get(job=job.id, type='TN').image
#         })
#     return render(request, 'jobs/portfolio.html', {'job_data': job_data})


class PortfolioPage(TemplateView):
    template_name = 'jobs/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_data = []
        jobs = Job.objects.order_by('-date_created')[:3]
        for job in jobs:
            # Will throw error if more than thumbnail image
            try:
                image = JobImage.objects.get(job_linked=job.id, is_thumbnail=True).image
            except JobImage.DoesNotExist:
                logger.info('No thumbnail image exists for Job: ', job)
                image = None
            job_data.append({
                'job': job,
                'image': image
            })
        context['job_data'] = job_data
        return context


def job_detail_page(request, slug):
    job = get_object_or_404(Job, url_slug=slug)
    images = JobImage.objects.filter(
        job_linked=job
    ).filter(
        is_thumbnail=None
    ).order_by(
        'order'
    )

    if job.title == 'Keyword Wrapper':
        template = 'jobs/keyword-wrapper.html'
    else:
        template = 'jobs/job_detail.html'

    context = {
        'job': job,
        'images': images,
    }
    return render(request, template, context)
