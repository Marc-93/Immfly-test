import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.services.logs.logger import Logger


class Waiter(object):
    def __init__(self, driver):
        self.driver = driver

    def presence_of_element(self, method, locator, stop=0.0, time_out=1):
        """Wait action until presence of an element.

        :param method: method to search the locator
        :param locator: locator identifier
        :param stop: stop hardcoded time
        :param time_out: max time out
        """
        # This param will allow to slow down the speed of framework actions that cannot be prevented on explicit wait
        if stop > 0:
            time.sleep(stop)
        try:
            WebDriverWait(self.driver, time_out).until(
                expected_conditions.presence_of_element_located(
                    (method, locator)))
        except:
            Logger(f"[wait] locator: {locator}, method: {method}, status: element NOT present").substep_passed()
