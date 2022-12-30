from src.shared_utils.logs.logger import Logger


def validate_data(current, expected, log="Result"):
    """Validates that current result is the same as expected result

    :param current: current result
    :param expected: obtained result
    :param log: log text
    """
    assert current == expected, Logger(f"[Result] current: {current}, expected: {expected}").substep_failed()
    Logger(f"[{log}] current: {current}, expected: {expected}").substep_passed()
