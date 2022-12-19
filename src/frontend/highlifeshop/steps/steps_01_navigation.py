from behave import *

from src.services.driver.actions.driver_action import driver_action
from src.services.logs.logger import Logger
from src.frontend.highlifeshop.steps.data.locators import *


def page_url(context, page):
    """Returns the url according to page selected

    :param context: framework param
    :param page: web page site
    :return: url
    """
    if page == "product_list":
        return context.site_url + "speedbird-cafe"
    else:
        Logger("[Web] Page not implemented!").substep_failed()


@step("User navigates to '{page}' page")
def ui_user_navigates_to_page(context, page):
    # Gets the complete url according to page defined in test
    context.driver.get(page_url(context, page))

    # Logs the result
    Logger(page_url(context, page)).substep_passed()


@step("User accepts the cookies")
def ui_user_accepts_cookies(context):
    # Gets the complete url according to page defined in test
    driver_action(context).click(element_info=cookies, stop=1, time_out=10)
