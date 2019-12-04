from django.test import TestCase
from django.urls import reverse, resolve

from datetime import datetime

from . import views

from .models import Job, JobImage


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
        self.assertEqual(view.func, views.portfolio_page)


class JobDetailPageTests(TestCase):

    def setUp(self):
        job = Job.objects.create(
            title='Test Job',
            url_slug='test-job',
            link_to_project='www.testjob.com',
            summary='Test Summary',
            body='Test Body',
            technologies=['java', 'python'],
            tags=None,
            date_created=datetime.now(),
            completed=True
        )
        url = reverse('job_detail', args=['test-job'])
        self.response = self.client.get(url)

    def test_portfolio_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # def test_portfolio_template(self):
    #     self.assertTemplateUsed(self.response, 'jobs/portfolio.html')
    #
    # def test_portfolio_contains_correct_html(self):
    #     self.assertContains(self.response, "Portfolio")
    #
    # def test_portfolio_resolves_url(self):
    #     view = resolve('/portfolio/')
    #     self.assertEqual(view.func, views.portfolio_page)
