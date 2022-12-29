from behave.model_core import Status

from src.services.logs.formatted_print import FormattedPrint
from src.services.qase.qase import Qase


def get_test_id(context):
    """ Get test if from tags from current test scenario.

    :param context: framework param
    """
    # Checks for all tags in current scenario if there is a param with qase value
    for tag in context.tags:
        if 'qase-' in str(tag).lower():
            # Formats the test id
            context.test_id = str(tag).lower().replace("qase-", "")
            break


def print_test_results(context, status):
    """Print results according to test status.

    :param context: framework param
    :param status: passed or failed
    """

    # If status is passed, this will print by console with formatted green color
    if status == Status.passed:
        context.test_result = "passed"
        try:
            FormattedPrint(f"TC-{context.test_id}", f"{str(context.test_result).upper()}").green()
        except:
            FormattedPrint(f"Test", f"{str(context.test_result).upper()}").green()

    # If status is failed, this will print by console with formatted red color
    if status == Status.failed:
        context.test_result = "failed"
        try:
            FormattedPrint(f"TC-{context.test_id}", f"{str(context.test_result).upper()}").red()
        except:
            FormattedPrint(f"Test", f"{str(context.test_result).upper()}").red()


def add_screenshot_failed_test(context, status):
    if status == Status.failed:
        context.driver_action.take_screenshot("step_failed")


def publish_qase_test_results(context):
    """Publish qase test results according to current test information.

    :param context: framework param
    """

    try:
        # Checks if qase value is ok to publish the results
        if context.initialize_qase is True:
            # Sends the request with test data
            Qase().publish_test_case(context.qase_run_id, context.test_id, context.test_result)
    except:
        FormattedPrint("Qase", "test not registered in Qase").pink()
