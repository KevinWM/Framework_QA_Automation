from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from base.base_test import BaseTest


class google_test(BaseTest):

    def test_google_search(self):

        # the page is ajaxy so the title is originally this:
        print self.driver.title

        # find the element that's name attribute is q (the google search box)
        inputElement = self.driver.find_element_by_name("q")

        # type in the search
        inputElement.send_keys("cheese!")

        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()

        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(self.driver, 10).until(EC.title_contains("cheese!"))

            # You should see "cheese! - Google Search"
            print self.driver.title

        finally:
            pass