from django.test import TestCase
from django.urls import reverse, resolve

from . import views


class HomepageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "George Christie")

    def test_homepage_resolves_url(self):
        view = resolve('/')
        self.assertEqual(view.func, views.home)
