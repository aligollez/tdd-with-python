from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        # resolve is the function Django uses internally to resolve URLS and find what view functions they should map to.
        # we are checking that resolve, when called with '/', the root of the site, finds a function called home_page
        # what function? it is the view function we're going to write which will return HTML
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # create an HttpRequest object, which is what Django will see when a user's browser asks for a page
        # pass it to out home_page view, which gives us a response.
        # extract the .content of the response. call .decode() to convert (raw bytes) into string of HTML
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
