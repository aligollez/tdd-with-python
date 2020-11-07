from selenium import webdriver

# starting a Selenium webdriver to open up a real Firefox browser window
# using it to open a web page we're expecting to served from the local PC
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# checking (making a test assertion) that the page has the word "Django" in its title
assert 'Django' in browser.title