from pyfiglet import Figlet

from src.services.db.db_actions import DataBase
from src.services.driver.hooks.devices import get_capabilities
from src.services.environment.command_line_params.execution_params import get_param_logs, active_logs, get_param_qase, \
    get_param_appium, set_android_home, set_appium, get_web_param_headless, get_ios_param_app_path, \
    get_ios_param_device, get_param_platform
from src.services.logs.formatted_print import FormattedPrint
from src.services.qase.qase import Qase


def print_test_execution_info():
    """Prints company name with ASCII art text"""
    custom_fig = Figlet(font='larry3d')
    print(custom_fig.renderText("IMMFLY"))


def set_execution_logs(context):
    # Gets the log param from test execution command (by default is not active)
    logs_status = get_param_logs(context)

    # Displays/hides the log
    active_logs(context, logs_status)


def set_db_connection(context):
    # starts the connection with schema
    context.db_connection = DataBase("template", context.server_name)


def set_execution_platform(context):
    # Depending on platform, sets the proper data needed

    get_param_platform(context)

    # web
    if context.platform == "web":
        # Gets the headless param from test execution command (by default is active)
        get_web_param_headless(context)

        # Sets the webapp url according to server
        context.site_url = "https://highlifeshop.com/"
        FormattedPrint("web", f"url --> {context.site_url}").pink()

        # Saves the needed capabilities before starting the web driver
        context.capabilities = {"url": context.site_url,
                                "headless": context.headless}

    # android
    elif context.platform == "android":
        # Gets the appium param to start or ignore the appium server
        get_param_appium(context)

        # Sets the android_home environment variable
        set_android_home()

        # According to appium variable, starts or not the appium server
        set_appium(context)

        # Saves the needed capabilities before starting the driver
        android_capabilities = {"platform": "android"}
        context.capabilities = get_capabilities(android_capabilities)

    # ios
    elif context.platform == "ios":
        # Gets the appium param to start or ignore the appium server
        get_param_appium(context)

        # Gets the app_path param from test execution command
        get_ios_param_app_path(context)

        # Gets the device param from test execution command
        get_ios_param_device(context)

        # According to appium variable, starts or not the appium server
        set_appium(context)

        # Saves the needed capabilities before starting the driver
        iphone_capabilities = {"platform": "ios",
                               "app_path": context.app_path,
                               "device": context.device}
        context.capabilities = get_capabilities(iphone_capabilities)


def set_qase_test_run(context):
    # Sets deactivated by default
    context.initialize_qase = False

    get_param_qase(context)

    try:
        if context.initialize_qase is True:
            # Send the request to create the test run
            context.qase_run_id = Qase().publish_test_run()

            # Prints the qase test run is created.
            FormattedPrint("Qase", "Publishing test suite on Qase!").pink()
        else:
            FormattedPrint("Qase", "Test results won't be published").pink()
    except:
        context.initialize_qase = False
        FormattedPrint("Qase", "Test results won't be published").pink()
