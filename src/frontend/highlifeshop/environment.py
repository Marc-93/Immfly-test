from src.services.driver.actions.driver_action import DriverActions
from src.services.driver.hooks.driver_setup import DriverSetup
from src.services.environment.e1_before_all import print_test_execution_info, set_execution_logs, \
    set_execution_platform, set_qase_test_run
from src.services.environment.e2_after_scenario import get_test_id, print_test_results, publish_qase_test_results, \
    add_screenshot_failed_test
from src.services.environment.e3_after_all import close_qase_test_run, generate_environment_file, generate_executor_file


def before_all(context):
    # Prints Bling with ASCII art text
    print_test_execution_info()

    # Sets log for test execution
    set_execution_logs(context)

    # Sets platform for test execution (web, android, iOS)
    set_execution_platform(context)

    # Sets qase publication for test execution (true: publish tests, false: not publish test)
    set_qase_test_run(context, "IMMFLY")


def before_scenario(context, scenario):
    # Sets the driver according to platform and capabilities
    context.driver = DriverSetup(context.platform).start_driver(context.capabilities)

    # Sets driver actions to perform the needed functions during tests
    context.driver_action = DriverActions(context.driver, context.platform)


def after_scenario(context, scenario):
    # Gets the test id from scenario tags
    get_test_id(context)

    # Prints the test results in terminal
    print_test_results(context, scenario.status)

    # Publish te results on qase if it is activated on before_all()
    publish_qase_test_results(context)

    # Adds a screenshot to test if it failed
    add_screenshot_failed_test(context, scenario.status)

    # Kills the driver at the end of the test
    DriverSetup(context.platform).kill_driver(context.driver)


def after_all(context):
    # Publish the last result from qase suite to close the test run
    close_qase_test_run(context)

    # Generates environment file for adding info in allure report
    generate_environment_file(context, "Immfly")

    # Generates executor file for adding info in allure report
    generate_executor_file(context)
