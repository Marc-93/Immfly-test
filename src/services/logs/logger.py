import allure
import logging


class Logger(object):
    def __init__(self, sub_step_title):
        self.step_info = sub_step_title

    def substep_passed(self):
        """Creates a sub-step log in allure report with <passed> status.
        """
        logging.info(self.step_info + "\n")
        with allure.step(self.step_info):
            print(self.step_info)
            pass

    def substep_failed(self):
        """Creates a sub-step log in allure report with <passed> status.
        """
        logging.warning(self.step_info + "\n")
        with allure.step(self.step_info):
            assert False, self.step_info
