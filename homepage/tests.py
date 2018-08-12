from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve

from homepage.views import index

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'homepage.views.index')

        request = HttpRequest()
        response = index(request)

        self.assertIn(b'hello world', response.content)

