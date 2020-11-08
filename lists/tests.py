from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        # resolve is the function Django uses internally to resolve URLS and find what view functions they should map to.
        # we are checking that resolve, when called with '/', the root of the site, finds a function called home_page
        # what function? it is the view function we're going to write which will return HTML
        found = resolve('/')
        self.assertEqual(found.func, home_page) 
