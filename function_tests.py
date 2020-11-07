from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user checking homepage
        self.browser.get('http://localhost:8000')

        # user notices page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
# starting a Selenium webdriver to open up a real Firefox browser window
# using it to open a web page we're expecting to served from the local PC

#User Story:
# User goes to check out the homepage
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# User notes the page title and head mention to-do lists
# assert 'To-Do' in browser.title, " Browser title was " + browser.title

# User is invited to enter a to-do item

# User types into a text box their first to-do 

# When user hits enter the page updates, and now the page lists users to-do item

# User sees unique URL for her -- to remember her list

# User visits that URL and see her to-do list still here

# checking (making a test assertion) that the page has the word "Django" in its title
# assert 'Django' in browser.title


# User finishes work and exits page
# browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')