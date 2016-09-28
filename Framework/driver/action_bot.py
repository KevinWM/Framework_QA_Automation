from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from configs.base_framework_configs import GlobalConfigsMessages as GM

from selenium import webdriver
from driver.browser_type import BrowserType


class ActionBot():
    """This class is an action-oriented abstraction over the Selenium APIs methods.

    :param browser_type: A string, Name of browser to use in the test
    """
    def __init__(self, browser_type):
        if browser_type != "":

            print(GM.SELECTED_BROWSER + browser_type)

            #Based on variable `browser_type` it select the correct driver
            if browser_type == BrowserType.FIREFOX:
                self.driver = webdriver.Firefox()
            elif browser_type == BrowserType.CHROME:
                self.driver = webdriver.Chrome()
            elif browser_type == BrowserType.IE:
                self.driver = webdriver.Ie()
            else:
                self.driver = None

            #Maximizes the current window that webdriver is using
            self.driver.maximize_window()

            #Delete all cookies in the scope of the session.
            self.driver.delete_all_cookies()

            #Tell WebDriver to poll the DOM for a certain amount of time when
            # trying to find an element if it is not immediately available
            self.implicitly_wait(2)

            #Set the amount of time to wait for a page load to complete before
            # throwing an error.
            self.set_page_load_timeout(5)
            print(GM.SELECTED_OPENED)

    def get_title(self):
        """
        Gets the title of the current page

        :return: Title of the page
        """
        return self.driver.title

    def get_driver(self):
        """
        Gets the driver object which is a instance of itself

        :return: ActionBot object
        """
        return self

    def get(self, url):
        """
        Loads a web page in the current browser session.

        :param url: A string, URL of the page to load
        """
        self.driver.get(url)

    def close(self):
        """
        Closes the current window.
        """
        self.driver.close()

    def quit(self):
        """
        Quits the driver and close every associated window.
        """
        self.driver.quit()

    def find_element(self, by=By.ID, value=None):
        """
        Finds element within this elements children by any locator

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: WebElement, if it found the element in the page
        """
        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None):
        """
        Finds a list of elements within this elements children by any locator

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: List of WebElement, if it found the element in the page
                 Empty list, if it does not found elements in the page that match the locator
        """
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        """
        Clicks an element.

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        """
        we = self.find_element(by, value)
        we.click()

    def clear(self, by, value):
        """
        Clears the text if it is a text entry element.

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        """
        we = self.find_element(by, value)
        we.clear()

    def get_attribute(self, by, value, attribute):
        """
        Gets the given attribute or property of the element.

        :param by: By object, Type of locator to used
        :param value: A string, Value of the locator in the page
        :param attribute: Attribute to look for
        :return:
        """
        we = self.find_element(by, value)
        we.get_attribute(attribute)

    def is_displayed(self, by, value):
        """
        Whether the element is visible to a user

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: True, if the element is visible to use
                 False, otherwise
        """
        we = self.find_element(by, value)
        return we.is_displayed()


    def is_enabled(self, by, value):
        """
        Returns whether the element is enabled

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: True, if the element is enable
                 False, otherwise
        """
        we = self.find_element(by, value)
        return we.is_enabled()

    def is_selected(self, by, value):
        """
        Returns whether the element is selected

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: True, if the element is selected
                 False, otherwise
        """
        we = self.find_element(by, value)
        return we.is_selected()

    def send_keys(self, by, value, word):
        """
        Simulates typing into the element.

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :param word: Word to type
        """
        we = self.find_element(by, value)
        we.send_keys(word)

    def get_element_text(self, by, value):
        """
        Gets the text of a element

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :return: Text of a element
        """
        we = self.find_element(by, value)
        return we.get_attribute('text')

    #*********** WAIT METHODS
    def implicitly_wait(self, seconds):
        """
        Sets a sticky timeout to implicitly wait for an element to be found,
        or a command to complete.
        This method only needs to be called one time per session. To set the
        timeout for calls to execute_async_script, see set_script_timeout.

        :param seconds: number of seconds to wait
        """
        self.driver.implicitly_wait(seconds)

    def set_page_load_timeout(self, seconds):
        """
        Set the amount of time to wait for a page load to complete
        before throwing an error.

        :param seconds: Number of seconds to wait
        """
        self.driver.set_page_load_timeout(seconds)

    def wait_for_element_present(self, by, value, seconds):
        """
        Wait a number of seconds for a element to be present in the page

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :param seconds: Number of seconds to wait
        :return: WebElement, if the element is found in the page
        """
        try:
            element = WebDriverWait(self.driver, seconds).until(
            EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            element = None

        return element

    def wait_for_element_visible(self, by, value, seconds):
        """
        Wait a number of seconds for a element to be visible in the page

        :param by: By object, Type of locator to use
        :param value: A string, Value of the locator in the page
        :param seconds: Number of seconds to wait
        :return: WebElement, if the element is visible in the page
        """
        element = WebDriverWait(self.driver, seconds).until(
        EC.visibility_of_element_located(by, value))
        return element

    def wait_for_title_present(self, title, seconds):
        """
        Wait until the title of a page is displayed
        title is the expected title, which must be an exact match

        :param title:
        :param seconds:
        :return: True, if the title matches,
                 False otherwise.
        """
        try:
            is_present = WebDriverWait(self.driver, seconds).until(
                EC.title_is(title))
        except TimeoutException:
            is_present = False
        return is_present

    def wait_for_title_contains(self, title, seconds):
        """
        Wait until the title of a page contains a case-sensitive
        substring. title is the fragment of title expected
        title is the expected title, which must be an exact match

        :param title:
        :param seconds:
        :return: True, if the title matches,
                 False otherwise.
        """
        try:
            is_present = WebDriverWait(self.driver, seconds).until(
                EC.title_contains(title))
        except TimeoutException:
            is_present = False
        return is_present