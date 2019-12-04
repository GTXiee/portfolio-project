from django.shortcuts import render
from django.views.generic import TemplateView

from jobs.models import Job, JobImage


#
# def home(request):
#     jobs = Job.objects.order_by('-date_created')[:3]
#     job_data = []
#     for job in jobs:
#         # Will throw error if more than thumbnail image
#         job_data.append({
#             'job': job,
#             'image': JobImage.objects.get(job=job.id, type='TN').image
#         })
#     return render(request, 'pages/home.html', {'job_data': job_data})


class HomepageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_data = []
        jobs = Job.objects.order_by('-date_created')[:3]
        for job in jobs:
            # Will throw error if more than thumbnail image
            try:
                image = JobImage.objects.get(job_linked=job.id, is_thumbnail=True).image
            except:
                image = None
            job_data.append({
                'job': job,
                'image': image
            })
        context['job_data'] = job_data
        return context
