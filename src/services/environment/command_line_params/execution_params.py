import logging
import os
import subprocess
import sys
import time

from src.services.environment.local_data import UserLocalData
from src.services.logs.formatted_print import FormattedPrint


def active_logs(context, status):
    """Activates or deactivates the logs on terminal depending on status param passed.

    :param context: framework param
    :param status: True or False
    """
    if not status:
        FormattedPrint("logs", "Hidden").pink()

    else:
        context._runner.teardown_capture()
        context._runner.stop_capture()
        context._runner.capture_controller.stdout_capture = sys.stdout

        logging.shutdown()
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s [%(name)s."
                   "%(funcName)s:%(lineno)d] %(message)s",
            datefmt="%H:%M:%S"
        )
        FormattedPrint("Logs", "Displayed").pink()


def get_param_logs(context):
    """Get the logs param from command line to activate or deactivate logs.
    Param not mandatory, by default logs are not active.

    :param context: framework param
    """
    try:
        logs_param = str(context.config.userdata['logs']).lower()
        print_logs = logs_param == "true"
        return print_logs
    except:
        return False


def get_param_platform(context):
    """Gets the platform param from command line, if param is not found it will be asked manually by terminal.
    This param is mandatory if it's wrong, the test will be stopped.

    :param context: framework param
    """
    # Creates the accepted platforms list
    platform_list = ['web', 'android', 'ios']
    try:
        # Gets the platform value from command line
        context.platform = str(context.config.userdata['platform']).lower()

        # Checks that platform is in accepted platforms list
        assert context.platform in platform_list, "[Platform] Not valid platform"

        # Prints the platform
        FormattedPrint("Platform", f"{context.platform}").pink()

    except:
        # When platform is invalid or not found, then ask through terminal to introduce manually the value
        FormattedPrint("Platform", "Platform not set correctly, please introduce it manually").pink()
        context.platform = input("Select platform:\n\033[38;5;211m   -Web\n   -Android\n   -iOS\n\033[0;0m").lower()

        # Checks that platform is in accepted platforms list
        if context.platform not in platform_list:
            FormattedPrint("Platform", "Incorrect platform variable").pink()

            # In case of platform is not in valid list, this will finish the test run
            exit()

        # Prints the platform
        FormattedPrint("Platform", f"{context.platform}").pink()


def get_param_appium(context):
    """Gets the appium param from command line to start or ignore appium.
    Param not mandatory, by default appium is not active.

    :param context: framework param
    """
    try:
        get_appium = str(context.config.userdata['appium']).lower()
        context.start_appium = get_appium == "true"
    except:
        context.start_appium = True


def get_web_param_headless(context):
    """Gets the headless param from command line to start browser with UI or not.
    Param not mandatory, by default headless is active.

    :param context: framework param
    """
    try:
        # Get the headless param from command line
        get_headless = str(context.config.userdata['headless']).lower()
        context.headless = get_headless == "true"
        FormattedPrint("web", f"headless --> {context.headless}").pink()
    except:
        context.headless = True
        FormattedPrint("web", f"headless --> {context.headless}").pink()


def set_android_home():
    """Checks if android_home environment variable is present.
    If not, this function will try to set with users present in yaml file.
    """
    # Tries to get the environment variable ANDROID_HOME
    android_home = os.getenv('ANDROID_HOME')

    # If ANDROID_HOME did not exist, then this process will set it by using user path in yaml file
    if android_home is None:
        os.environ['ANDROID_HOME'] = UserLocalData().get_local_data("ANDROID_HOME")
        FormattedPrint("Android",
                       f"ANDROID_HOME not found, set environment variable: {os.getenv('ANDROID_HOME')}").pink()
    else:
        FormattedPrint("Android", f"ANDROID_HOME: {os.getenv('ANDROID_HOME')}").pink()


def get_ios_param_app_path(context):
    """Gets the app_path param from command line to get the installer application file.
    Param mandatory, if it's not present this function will try to get by users present in yaml file.

    :param context: framework param
    """
    try:
        context.app_path = str(context.config.userdata['app_path']).lower()
        FormattedPrint("iOS", f"app_path: {context.app_path}").pink()
    except:
        # If app_path did not exist, then this process will set it by using user path in yaml file
        context.app_path = UserLocalData().get_local_data("APP_PATH")


def get_ios_param_device(context):
    """Gets the device param from command line to get test device.
    Param mandatory, if it's not present iphone 13 will be the default value.

    :param context: framework param
    """
    try:
        # Gets the device from command line
        # Formats the _ by withe space due is not allowed to pass withe spaces by command line
        context.device = str(context.config.userdata['device']).replace("_", " ")
    except:
        # If device is not passed, then sets Iphone 13 as default
        context.device = "iPhone 13"

    FormattedPrint("iOS", f"device: {context.device}").pink()


def set_appium(context):
    """Starts appium server according to param get from appium command.

    :param context: framework param
    """
    # If start appium is true, then launches all the commands needed for starting the appium
    if context.start_appium is True:
        # Sometimes appium nodes are locked, then before starting the tests we try to kill them to prevent some issues.
        subprocess.Popen(["killall", "node"]).wait()
        # subprocess.Popen(["adb", "start-server"])
        # Starts the appium service to open the communication with device
        subprocess.Popen(["appium", "--log-level", "error", "--port", "4723"])
        # Waits to start the appium server
        time.sleep(3)


def get_param_qase(context):
    """Gets the qase param from command line to publish or not the results.
        Param not mandatory, by default is not active.

        :param context: framework param
        """
    try:
        # Gets the qase param from command line
        get_qase = str(context.config.userdata['qase']).lower()

        # Checks the param received from command line
        context.initialize_qase = get_qase == "true"

    except:
        # if something went wrong, qase test results won't be published
        context.initialize_qase = False
