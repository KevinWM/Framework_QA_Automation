import time

from base.base_test import BaseTest
from page_objects.login_page.gmail_login_page import GmailLoginPage
from configs.base_framework_configs import GlobalConfigs as GC
from configs.base_framework_configs import GlobalConfigsMessages as GM


class LoginTestSuite(BaseTest):

    def test_log_in(self):
        """
        Given: A user with valid credentials
        When: Request to log in Gmail
        Then: User is able to access his/her Inbox successfully
        """

        #Create instance of Login page, which is the initial page
        gmail_login_page = GmailLoginPage(self.driver)

        #Validate the page title is displayed
        self.assertTrue(gmail_login_page.is_title_displayed(), GM.ERROR_GMAIL_PAGE)

        #Enter the user email in the correct field
        gmail_login_page.enter_email(GC.USER_EMAIL)

        #Check if the next button is displayed, if it is displayed the password field
        #is not present until it clicks on next button
        if gmail_login_page.exist_next_button():
            gmail_login_page.click_next_button()

        #Enter user password in the correct field
        gmail_login_page.enter_password(GC.USER_PASSWORD)

        #Click on Sign In button and returns the new page = Inbox
        inbox_page = gmail_login_page.click_sign_in_button()

        #Check the Inbox page title is displayed
        self.assertTrue(inbox_page.is_title_displayed(), GM.ERROR_INBOX_PAGE)

        #To be sure the Inbox page is displayed, it validates the COMPOSE button is displayed
        self.assertTrue(inbox_page.is_compose_button_displayed(), GM.ERROR_INBOX_COMPOSE_BUTTON)

        #It is not needed, just added to avoid inbox page closes so fast
        time.sleep(5)