from behave import *

from src.services.driver.actions.driver_action import driver_action
from src.frontend.highlifeshop.steps.data.locators import *


@step("User selects sorter selector")
def ui_user_selects_sorter_selector(context):
    # Gets the complete url according to page defined in test
    driver_action(context).click(element_info=sort_by, stop=0, time_out=4)


@step("User validates sorting options")
def ui_user_validates_sorting_options(context):
    # Gets the complete url according to page defined in test
    driver_action(context).select_option_by_value(element_info=sort_by, value="position", stop=1, time_out=2)
    driver_action(context).select_option_by_value(element_info=sort_by, value="name", stop=1, time_out=2)
    driver_action(context).select_option_by_value(element_info=sort_by, value="price", stop=1, time_out=2)
    driver_action(context).select_option_by_value(element_info=sort_by, value="new", stop=1, time_out=2)
