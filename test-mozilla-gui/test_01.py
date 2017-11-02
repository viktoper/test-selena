import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
#        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://docs.python.org/3/tutorial/index.html")
#        google_find_box = driver.find_element_by_id("sfdiv")
#        google_find_box.send_keys("Бриллиантовая рука"+Keys.RETURN)
        try:
            google_br_link = driver.find_element_by_link_text('3.1.1. Numbers')
            print("Link '3.1.1. Numbers' found!")
            google_br_link.click()
        except Exception:
            print("Link '3.1.1. Numbers' not found!")

        try:
            google_br_link = driver.find_element_by_name("3.1.2. Strings")
            print("Text '3.1.2. Strings' found!")
        except Exception:
            print("Text '3.1.2. Strings' not found! on page")
            


#        google_br_link = driver.find_elements_by_partial_link_text("Бриллиантовая рука — Википедия")
#        driver.find_elements_by_partial_link_text("Бриллиантовая рука — Википедия").click()

#        for option in google_br_link:
#            print("Value is: %s" % option.get_attribute("value"))

#        self.assertIn("Python", driver.title)
#        menu_about = driver.find_element_by_name("About")
#        assert "No results for About." not in driver.page_source
#        menu_about.send_keys(Keys.RETURN)
#        menu_getting_started = driver.find_element_by_name("Getting Started")
 #       assert "No results for Getting Started." not in driver.page_source
#        menu_about.send_keys(Keys.RETURN)

#        elem = driver.find_element_by_name("q")
#        elem.send_keys("pycon")
#        assert "No results found." not in driver.page_source
#        elem.send_keys(Keys.RETURN)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
