from behave import *

from src.services.driver.actions.driver_action import driver_action
from src.frontend.functionality.steps.data.locators import *
from src.services.logs.logger import Logger


@step("Preconditions")
def ui_preconditions(context, page):
    # preconditions
    pass


@step("User action <action>")
def ui_user_action(context, action):
    # clicks on the option set
    driver_action(context).click(element_info=locator, 
                                 stop=1, 
                                 time_out=10)


@step("User accepts the cookies")
def ui_user_validations(context):
    # Asserts the results
    assert 1 == 1, Logger(f"[Result] expected: x, current: y").substep_failed()

    Logger(f"[Result] expected: x, current: x").substep_passed()
