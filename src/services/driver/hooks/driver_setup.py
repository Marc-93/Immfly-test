from src.services.driver.hooks.appium_hooks import AppiumHooks
from src.services.driver.hooks.selenium_hooks import SeleniumHooks


class DriverSetup(object):
    def __init__(self, platform):
        self.platform = platform

    def start_driver(self, capabilities):
        """Start driver using the selected capabilities for test execution.

        :param capabilities: desired params for each platform.
        :return: driver
        """
        if self.platform == 'android' or self.platform == 'ios':
            return AppiumHooks().start_appium_app(capabilities)
        elif self.platform == 'web':
            return SeleniumHooks().start_web_driver(capabilities)

    def kill_driver(self, driver):
        """Kill driver session.

        :param driver: driver
        """
        if self.platform == 'android' or self.platform == 'ios':
            AppiumHooks().kill_appium_app(driver)
        elif self.platform == 'web':
            SeleniumHooks().kill_web_driver(driver)
