from django.test import TestCase
from django.urls import reverse, resolve

from . import views


class ContactPageTests(TestCase):

    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contact_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_page_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_page.html')

    def test_contact_page_contains_correct_html(self):
        self.assertContains(self.response, "Contact")

    def test_contact_page_resolves_url(self):
        view = resolve('/contact/')
        self.assertEqual(view.func, views.contact_page)


class ThanksPageTests(TestCase):

    def setUp(self):
        url = reverse('thanks')
        self.response = self.client.get(url)

    def test_thanks_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_thanks_page_template(self):
        self.assertTemplateUsed(self.response, 'contact/thanks_page.html')

    def test_thanks_contains_correct_html(self):
        self.assertContains(self.response, "Thanks")

    def test_thanks_resolves_url(self):
        view = resolve('/contact/thanks/')
        self.assertEqual(view.func, views.thanks_page)
