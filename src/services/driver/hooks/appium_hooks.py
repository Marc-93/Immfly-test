from appium import webdriver

from appium.webdriver.appium_service import AppiumService


def connect_driver(capabilities):
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)


class AppiumHooks:

    def start_appium_app(self, capabilities):
        """Starts appium server by setting the selected capabilities in environment file.

        :param capabilities: android or iOS options
        :return: driver
        """
        # Open the device application
        driver = connect_driver(capabilities)

        # Hiding keyboard to avoid failures between tests
        driver.hide_keyboard()

        return driver

    def kill_appium_app(self, driver):
        """Killing driver and appium session.

        :param driver: driver
        """

        # Killing driver
        driver.quit()

        # Killing appium session
        AppiumService().stop()
