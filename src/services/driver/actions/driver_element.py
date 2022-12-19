import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from src.services.logs.logger import Logger
from src.services.driver.actions.driver_wait import Waiter


class Element(object):
    def __init__(self, driver, platform):
        """All type of functions to interact with UI.

        :rtype: platform driver
        """
        self.driver = driver
        self.platform = platform

    def __get_locator(self, element_info):
        """Gets the locator according to proper platform

        :param element_info: locator dictionary with all platforms and methods
        :return: locator for platform used
        """
        return element_info[self.platform]['locator']

    def __get_method(self, element_info):
        """Gets the method according to proper platform

        :param element_info: locator dictionary with all platforms and methods
        :return: method for platform used
        """
        if self.platform == "web":
            if element_info[self.platform]['method'] == 'id':
                return By.ID
            elif element_info[self.platform]['method'] == 'class':
                return By.CLASS_NAME
            elif element_info[self.platform]['method'] == 'name':
                return By.NAME
            elif element_info[self.platform]['method'] == 'css':
                return By.CSS_SELECTOR
            elif element_info[self.platform]['method'] == 'xpath':
                return By.XPATH
            else:
                Logger("[Method] Selenium method not implemented!").substep_failed()

        if self.platform == "android" or self.platform == "ios":
            if element_info[self.platform]['method'] == 'id':
                return AppiumBy.ID
            elif element_info[self.platform]['method'] == 'class':
                return AppiumBy.CLASS_NAME
            elif element_info[self.platform]['method'] == 'name':
                return AppiumBy.NAME
            elif element_info[self.platform]['method'] == 'xpath':
                return AppiumBy.XPATH
            elif element_info[self.platform]['method'] == 'accessibility_id':
                return AppiumBy.ACCESSIBILITY_ID
            else:
                Logger("[Method] Appium method not implemented!").substep_failed()

    def get_element(self, element_info, stop=0.0, time_out=1):
        """Finds element of current view.

        :param element_info: method + locator
        :param stop: stop hardcoded time
        :param time_out: max time out
        :return: find_element
        """
        method = self.__get_method(element_info)
        locator = self.__get_locator(element_info)

        Waiter(self.driver).presence_of_element(method, locator, stop, time_out)
        return self.driver.find_element(method, locator)

    def __visibility(self, element_info, stop=0.0):
        """Gets the element visibility.

        :param element_info: method + locator
        :param stop: stop hardcoded time
        :return: boolean status
        """
        try:
            return Element(self.driver, self.platform).get_element(element_info, stop).is_displayed()
        except:
            return False

    def displayed(self, element_info, stop=0.0, time_out=1):
        """Gets the displayed status of specific element into current view.

        :param element_info: method + locator
        :param stop: stop hardcoded time
        :param time_out: max time out
        :return: boolean status
        """
        status = self.__visibility(element_info, stop)
        while status is False:
            status = self.__visibility(element_info, stop=0)
            time_out -= 1
            time.sleep(1)
            if time_out <= 0:
                break

        Logger(f"[element] locator: {element_info[self.platform]['locator']}, displayed: {status}").substep_passed()
        return status

    def selected(self, element_info, stop=0.0, time_out=1):
        """Gets the selected status of specific element into current view.

        :param element_info: method + locator
        :param stop: stop hardcoded time
        :param time_out: max time out
        :return: boolean status
        """
        status = False
        try:
            status = Element(self.driver, self.platform).get_element(element_info, stop, time_out).is_selected()
            Logger(f"[element] locator: {element_info[self.platform]['locator']}, selected: {status}").substep_passed()
            return status
        except:
            return status
