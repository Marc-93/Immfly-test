from selenium.webdriver import ActionChains

from src.services.logs.logger import Logger
from src.services.driver.actions.driver_element import Element


def scroll_action(context):
    return Scroll(context.driver, context.platform)


class Scroll(object):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform
        self.element = Element(self.driver, self.platform)

    def down(self):
        """Performs a scroll down into current view."""
        if self.platform == "web":
            try:
                # Goes to the bottom to the current page with javascript action.
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                Logger(f"[scroll] direction: down, result: success").substep_passed()
            except:
                Logger(f"[scroll] direction: down, result: failed").substep_failed()

        elif self.platform == "android" or self.platform == "ios":
            try:
                # find the current device resolution
                # Set height and width to half to get the middle point of the screen.
                # o = origin / d = destination
                o_x = self.driver.get_window_size()['width'] / 2
                o_y = self.driver.get_window_size()['height'] / 2
                d_x = o_x
                # Reduces the origin point to create a destination point lower than origin
                d_y = o_y - (o_y * o_y/2)
                self.driver.swipe(o_x, o_y, d_x, d_y)
                Logger(f"[scroll] direction: down, result: success").substep_passed()
            except:
                Logger(f"[scroll] direction: down, result: failed").substep_failed()

    def up(self):
        """Performs a scroll up into current view."""
        if self.platform == "web":
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
                Logger(f"[scroll] direction: up, result: success").substep_passed()
            except:
                Logger(f"[scroll] direction: up, result: failed").substep_failed()

        elif self.platform == "android" or self.platform == "ios":
            try:
                # find the current device resolution
                # Set height and width to half to get the middle point of the screen.
                # o = origin / d = destination
                o_x = self.driver.get_window_size()['width'] / 2
                o_y = self.driver.get_window_size()['height'] / 2
                d_x = o_x
                # Increases the origin point to create a destination point lower than origin
                d_y = o_y + (o_y * o_y/2)
                self.driver.swipe(o_x, o_y, d_x, d_y)
                Logger(f"[scroll] direction: up, result: success").substep_passed()
            except:
                Logger(f"[scroll] direction: up, result: failed").substep_failed()

    def execute_scroll(self, direction):
        """Executes scrolls in the specified direction.

        :param direction: up, down
        """

        if direction == "down":
            self.down()
        elif direction == "up":
            self.up()

    def move_to_element(self, element_info, stop=0, time_out=1):
        """Moves the current view with scroll action to expected element.

        :param element_info: method + locator
        :param stop: break time
        :param time_out: maximum time out
        """
        element = self.element.get_element(element_info, stop, time_out)

        if self.platform == "web":
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                Logger(f"[scroll] scroll to element: done!").substep_passed()
            except:
                Logger(f"[scroll] scroll to element: failed!").substep_failed()

        elif self.platform == "android" or self.platform == "ios":
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element)
                Logger(f"[scroll] element visible on screen").substep_passed()
            except:
                Logger(f"[scroll] element NOT visible on screen").substep_failed()

    def swipe_inside_element(self, element_info, direction="down", stop=0, time_out=1):
        """Swipes the screen to specified direction to scroll inside an element.

        :param element_info: method + locator
        :param direction: direction to swipe
        :param stop: break time
        :param time_out: maximum time out
        """
        if self.platform == "android" or self.platform == "ios":
            element = self.element.get_element(element_info, stop, time_out)
            try:
                # find the current device resolution
                # Set height and width to half to get the middle point of the screen.
                # o = origin / d = destination
                # Adds some extra space to avoid the margins of the screen.
                o_x = element.location['x'] + 10
                o_y = element.location['y'] + 10
                d_x = o_x
                if direction == "up":
                    # Increases the origin point to create a destination point lower than origin
                    d_y = o_y + (o_y * o_y/2)
                elif direction == "down":
                    # Reduces the origin point to create a destination point lower than origin
                    d_y = o_y - (o_y * o_y/2)
                else:
                    d_y = o_y - 1500

                self.driver.swipe(o_x, o_y, d_x, d_y)
                Logger(f"[swipe] scroll inside element: {direction}, result: success").substep_passed()
            except:
                Logger(f"[swipe] scroll inside element: failed").substep_failed()
