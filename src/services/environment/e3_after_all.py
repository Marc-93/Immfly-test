import os
import subprocess

from src.services.logs.formatted_print import FormattedPrint
from src.services.qase.qase import Qase


def close_qase_test_run(context):
    """Completes the test run by passing the last test.

    :param context: framework param
    """

    # Checks if qase value is ok to publish the results
    if context.initialize_qase is True:
        # Sends the request with last test case forced to passed status.
        Qase().publish_test_case(context.qase_run_id, 1, "passed")

        # Sets the public qase link from test run
        # It runs a request to get the public link
        context.qase_url = Qase().make_public_results(context.qase_run_id)

        # Prints the qase info
        FormattedPrint("Qase", "Closed test suite on Qase!").pink()
        FormattedPrint("Qase", f"Find the public report here: {context.qase_url}").pink()


def generate_environment_file(context, platform):
    """Creates an environment file to add some data in allure reporter.

    :param context: framework param
    :param platform: Backend, Android, iOS, Web
    """

    # Creates the file in allure results, depending on qase info
    try:
        output_path = (os.getenv('APP_HOME') or '.') + '/src/allure/environment.properties'

        # If qase is active, this will display the qase public report on allure
        if context.initialize_qase is True:
            with open(output_path, 'w') as f:
                f.write(F'Platform=web\nUrl=https://highlifeshop.com/speedbird-cafe\nQase={context.qase_url}')

        # If qase is not active, this will display a message saying that qase is not published.
        elif context.initialize_qase is False:
            with open(output_path, 'w') as f:
                f.write(F'Platform=web\nUrl=https://highlifeshop.com/speedbird-cafe\nQase=Test run not published')
    except Exception as e:
        print(e)
        FormattedPrint("Allure", "Environment not created").pink()


def generate_executor_file(context):
    """Generates an executor file to add the info in allure report.

    :param context: framework param
    """
    try:
        # gets the executor by command line
        executor = context.config.userdata['executor']
    except:
        # If executor does not exist, sets jenkins as default
        executor = "Marc AC"

    try:
        # Creates file for adding executor information into allure
        with open('src/allure/executor.json', 'w') as f:
            f.write("{" + f'\n"name": "{executor}",\n'
                          f'"type": "jenkins",\n'
                          f'"buildName": "allure-report_deploy",\n'
                          f'"buildUrl": "https://www.jenkins.io//"\n' + "}")
    except:
        FormattedPrint("Allure", "Executor not created").pink()


def close_connections(context):
    """Kills all the connections to prevent leaving ports opened.

    :param context: framework param
    """
    if context.platform == "android" or context.platform == "ios":
        subprocess.Popen(["killall", "node"]).wait()
