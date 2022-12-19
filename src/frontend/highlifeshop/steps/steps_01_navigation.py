from behave import *

from src.services.logs.logger import Logger


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