from unittest import TestCase

from configs.base_framework_configs import GlobalConfigs as GC
from driver.action_bot import ActionBot


class BaseTest(TestCase):


    def setUp(self):

        #Create the instance of ActionBot class
        self.action_bot = ActionBot(GC.BROWSER)

        #driver is an ActionBot object
        self.driver = self.action_bot.get_driver()
        self.url = GC.URL

        #Types the ulr page in the current browser session
        self.driver.get(self.url)
        

    def tearDown(self):

        #Quits the driver and close every associated window.
        self.driver.quit()

