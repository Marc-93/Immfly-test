import allure
from selenium.webdriver import Keys

from src.services.logs.formatted_print import FormattedPrint
from src.services.logs.logger import Logger
from src.services.driver.actions.driver_element import Element
from src.services.driver.actions.driver_scroll import Scroll


def driver_action(context):
    # driver_action = lambda driver, platform : driver_actions(driver, platform)
    return DriverActions(context.driver, context.platform)


class DriverActions(object):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform
        self.element = Element(self.driver, self.platform)
        self.scroll = Scroll(self.driver, self.platform)

    def click(self, element_info, stop=0.0, time_out=1):
        """Clicks the element selected.

        :param element_info: method + locator
        :param stop: stop hardcoded time
        :param time_out: max time out
        """
        try:
            self.element.get_element(element_info, stop, time_out).click()
            Logger(f"[click] locator: {element_info[self.platform]['locator']}, result: clicked").substep_passed()
        except:
            Logger(f"[click] locator: {element_info[self.platform]['locator']}, result: not clicked").substep_failed()

    def type(self, element_info, text, stop=0.0, time_out=1):
        """Types into element selected.

        :param element_info: method + locator
        :param text: text to type
        :param stop: stop hardcoded time
        :param time_out: max time out
        """
        try:
            self.element.get_element(element_info, stop, time_out).send_keys(text)
            Logger(f"[type] locator: {element_info[self.platform]['locator']}, text: {text}, result: typed")\
                .substep_passed()
        except:
            Logger(f"[type] locator: {element_info[self.platform]['locator']}, text: {text}, result: not typed")\
                .substep_failed()

    def clear_password(self, element_info, retries=4, stop=0.0, time_out=1):
        """Clearing the password field by clicking backspace key.

        :param element_info: method + locator
        :param retries: times to repeat the action
        :param stop: stop hardcoded time
        :param time_out: max time out
        """
        try:
            for iteration in range(retries):
                self.element.get_element(element_info, stop, time_out).send_keys(Keys.BACKSPACE)
            Logger(f"[clear] - locator: {element_info[self.platform]['locator']}, result: clean")\
                .substep_passed()
        except:
            Logger(f"[clear] - locator: {element_info[self.platform]['locator']}, result: nothing to clean")\
                .substep_passed()

    def scroll_to_element(self, element_info, max_scrolls=10, direction="down", stop=0, time_out=1):
        """Executes scrolls until element is found or maximum of scrolls allowed.

        :param element_info: method + locator
        :param max_scrolls: maximum scrolls
        :param direction: direction of scroll
        :param stop: stop time
        :param time_out: max time out
        """
        Logger("SCROLL TO ELEMENT --->").substep_passed()

        # Checks if element is present:
        # - Present: skips the scroll action
        # - Not present: performs scrolls
        element_present = self.element.displayed(element_info, stop, time_out)

        while element_present is False:
            self.scroll.execute_scroll(direction)
            max_scrolls -= 1
            element_present = self.element.displayed(element_info, stop, time_out)
            if max_scrolls <= 0:
                break

        # Moves to element if it's present in the screen.
        if element_present is True:
            self.scroll.move_to_element(element_info, stop=0, time_out=0)

        return element_present

    def take_screenshot(self, step_info="screenshot"):
        """Adds screenshot to allure report.

        :param step_info: name of screenshot file
        """
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=step_info,
                          attachment_type=allure.attachment_type.PNG)
            FormattedPrint("Allure", "Screenshot saved").pink()
        except:
            FormattedPrint("Allure", "Screenshot not saved").pink()

    def validate_element(self, element_info, max_scrolls=10, direction="down", stop=0, time_out=1):
        """Creates a consecutive generic actions that validates if element exists and prints the proper logs.

        :param element_info: method + locator
        :param max_scrolls: maximum scrolls to search the element
        :param direction: direction of scroll
        :param stop: stop hardcoded time
        :param time_out: max time out
        """
        # Scrolls to the element, returns if it's present
        if max_scrolls == 0:
            element = self.element.displayed(element_info, stop, time_out)
        else:
            element = self.scroll_to_element(element_info, max_scrolls, direction)

        # Takes a screenshot
        self.take_screenshot(element_info[self.platform]['locator'])

        # Checks if element status is the same as expected (visible)
        assert element is True, Logger(f"[assert] {element_info[self.platform]['locator']} visible != True")\
            .substep_failed()
        Logger(f"[assert] {element_info[self.platform]['locator']} visible == True")\
            .substep_passed()

    def user_binding(self, success = True ):
        if self.platform == 'android' and success is True:
            self.driver.finger_print(1)
        elif self.platform == 'ios' and success is True:
            self.driver.touch_id(True)

        elif self.platform == 'android' and success is False:
            self.driver.finger_print(10)
            self.driver.finger_print(10)
            self.driver.finger_print(10)
            self.driver.finger_print(10)
            self.driver.finger_print(10)
            self.driver.finger_print(10)
        elif self.platform == 'ios' and success is False:
            self.driver.touch_id(False)
