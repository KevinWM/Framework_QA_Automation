from selenium.webdriver.common.by import By

class InboxLocators():
    """
    Class that contains the Locators of the web elements
    """
    def __init__(self):
        pass

    TITLE = "Inbox"
    INBOX_UNREAD_LABEL = (By.XPATH, "//span/a[contains(text(),'Inbox')]")
    GMAIL_TOP_LABEL = (By.XPATH, "//div[@id=':j']/span[.='Gmail']")
    COMPOSE_BUTTON = (By.XPATH, "//div[text()='COMPOSE']")


class InboxPage():
    """
    Class that contains the actions of the web elements in the Inbox page

    :param driver: Driver to manage the page and elements
    """
    def __init__(self, driver):
        self.driver = driver

    def is_title_displayed(self):
        """
        Check if the page title is displayed

        :return: True, if the correct title is displayed
                 False, otherwise
        """
        return self.driver.wait_for_title_contains(InboxLocators.TITLE, 30)

    def is_compose_button_displayed(self):
        """
        Check if the COMPOSE button is displayed in the page
        :return: True, if the botton is displayed
                 False, otherwise
        """
        result = True
        we = self.driver.wait_for_element_present(InboxLocators.COMPOSE_BUTTON[0], InboxLocators.COMPOSE_BUTTON[1], 20)

        if we is None:
            result = False

        return result