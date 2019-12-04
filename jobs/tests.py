from django.test import TestCase
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile

from datetime import datetime

from . import views

import mock

from .models import Job, JobImage
from taggit.models import Tag


class PortfolioPageTests(TestCase):

    def setUp(self):
        url = reverse('portfolio')
        self.response = self.client.get(url)

    def test_portfolio_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_portfolio_template(self):
        self.assertTemplateUsed(self.response, 'jobs/portfolio.html')

    def test_portfolio_contains_correct_html(self):
        self.assertContains(self.response, "Portfolio")

    def test_portfolio_resolves_url(self):
        view = resolve('/portfolio/')
        self.assertEqual(view.func.__name__, views.PortfolioPage.as_view().__name__)


class JobDetailPageTests(TestCase):

    def setUp(self):
        self.job = Job.objects.create(
            title='Test Job',
            url_slug='test-job',
            link_to_project='www.testjob.com',
            summary='Test Summary',
            body='Test Body',
            technologies=['python'],
            tags=[Tag(name='python')],
            date_created=datetime.strptime('2018-12-30 09:00:00', '%Y-%m-%d %H:%M:%S'),
            completed=True
        )
        # self.thumbnail_file = SimpleUploadedFile('thumbnail_file',
        #                                          open(test_image_path, 'rb').read(),
        #                                          content_type='image/jpeg')
        # JobImage.objects.create(
        #     job_linked=self.job,
        #     image=self.thumbnail_file,
        #     is_thumbnail=True,
        #     order=0
        # )

    def test_job_listing(self):
        self.assertEqual(self.job.title, 'Test Job')
        self.assertEqual(self.job.url_slug, 'test-job')
        self.assertEqual(self.job.link_to_project, 'www.testjob.com')
        self.assertEqual(self.job.summary, 'Test Summary')
        self.assertEqual(self.job.body, 'Test Body')
        self.assertEqual(self.job.technologies, ['python'])
        self.assertEqual(self.job.tags[0].name, 'python')
        self.assertEqual(self.job.date_created, datetime.strptime('2018-12-30 09:00:00', '%Y-%m-%d %H:%M:%S'))
        self.assertEqual(self.job.completed, True)

    def test_job_detail_view(self):
        response = self.client.get(self.job.get_absolute_url())
        no_response = self.client.get('/portfolio/this_should_404/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Job')
