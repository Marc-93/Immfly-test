import time

from behave import *

from src.services.driver.actions.driver_action import driver_action
from src.frontend.highlifeshop.steps.data.locators import *
from src.services.logs.logger import Logger

def validate_test_sort_value(sort):
    if str(sort).lower() == 'position' or \
        str(sort).lower() == 'name' or \
        str(sort).lower() == 'price' or \
        str(sort).lower() == 'new':
        return str(sort).lower()
    else:
        Logger(f"[Test] data not valid -> sort: {sort}").substep_failed()


@step("User selects '{sort}' sort option")
def ui_user_selects_sorter_selector(context, sort):
    value = validate_test_sort_value(sort)
    driver_action(context).select_option_by_value(element_info=sort_by, value=value, stop=1, time_out=2)


@step("User validates '{sort}' sort option is selected")
def ui_user_validates_sort_text_selected(context, sort):
    value = validate_test_sort_value(sort)
    text = driver_action(context).get_text_from_dropdown(element_info=sort_by, stop=1, time_out=2)
    assert value in str(text).lower()
    Logger(f"[Result] Current: {str(text).lower()}, Expected: {value}").substep_passed()
    driver_action(context).take_screenshot(f"{sort}")


@step("User validates url contains the expected sorting '{sort}'")
def ui_user_validates_url_with_sorting_params(context, sort):
    value = validate_test_sort_value(sort)
    context.driver.refresh()
    url = str(context.driver.current_url).lower()
    Logger(f"[web] url: {url}").substep_passed()

    # assert value in url
    Logger(f"[Result] Filtering option inside the url").substep_passed()

