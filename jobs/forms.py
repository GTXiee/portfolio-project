from django.forms import ModelForm, ModelChoiceField

from .models import Job, JobImage


# class JobForm(ModelForm):
#     class Meta:
#         model = Job
#         fields = [
#             'title',
#             'url_slug',
#             'link_to_project',
#             'summary',
#             'thumbnail_image',
#             'body',
#             'technologies',
#             'tags',
#             'date_created',
#             'completed'
#         ]
#         field_classes = {
#             'thumbnail_image': ModelChoiceField(queryset=JobImage.objects.filter(job=))
#         }

