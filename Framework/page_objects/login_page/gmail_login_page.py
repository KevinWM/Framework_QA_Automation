from selenium.webdriver.common.by import By
from page_objects.inbox_page.inbox_page import InboxPage


class LoginLocators():
    """
    Class that contains the Locators of the web elements
    """

    def __init__(self):
        pass

    TITLE = "Gmail"
    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Passwd')
    SING_IN_BUTTON = (By.ID, 'signIn')
    NEXT_BUTTON = (By.ID, 'next')


class GmailLoginPage():
    """
    Class that contains the actions of the web elements in the login page

    :param driver: Driver to manage the page and elements
    """

    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        """
        Check if the tile is displayed in the page

        :return: True, if the title is displayed
                 False, otherwise
        """
        return self.driver.wait_for_title_present(LoginLocators.TITLE, 30)

    def enter_email(self, email):
        """
        Types the user email

        :param email: A string, user email
        """
        self.driver.send_keys(LoginLocators.EMAIL_INPUT[0], LoginLocators.EMAIL_INPUT[1], email)

    def enter_password(self, passw):
        """
        Types the user password

        :param passw: A string, user password
        """
        self.driver.send_keys(LoginLocators.PASSWORD_INPUT[0], LoginLocators.PASSWORD_INPUT[1], passw)

    def click_next_button(self):
        """
        Clicks on Next button located after the username is displayed (it does not appear always)
        """
        self.driver.click(*LoginLocators.NEXT_BUTTON)

    def exist_next_button(self):
        """
        Check if the Next button is displayed in the page

        :return: True, if the button is displayed
                 False, otherwise
        """
        result = True
        we = self.driver.find_elements(*LoginLocators.NEXT_BUTTON)
        if len(we) is 0:
            result = False
        return result

    def click_sign_in_button(self):
        """
        Clicks on Sing In button to access the Inbox page
        :return: InboxPage Page object
        """
        self.driver.click(*LoginLocators.SING_IN_BUTTON)
        return InboxPage(self.driver)
