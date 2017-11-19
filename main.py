import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://54.213.123.161:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX.copy())

    def test_google_page(self):
        driver = self.driver
        driver.get("https://google.com/")
        tutorial = driver.title
        print(tutorial)
        self.assertEqual("Google", tutorial)
        print(driver.capabilities['browserName'])

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()