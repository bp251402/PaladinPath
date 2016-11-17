# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        This website explores the interface between Modern American Catholicism and the birthplace of fantasy
        role-playing games, Dungeons and Dragons, through the connecting point of the Paladin class.

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Paladin Path',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('bestphoto.JPG',m.get_attribute('src'))

        a=self.browser.find_element_by_id('AngelicAvenger')
        a.click()

        self.assertIn('AngelicAvenger', self.browser.title)

        h=self.browser.find_element_by_tag_name('h1')
        m=self.browser.find_element_by_tag_name('img')


if __name__=="__main__":
        unittest.main(warnings="ignore")
