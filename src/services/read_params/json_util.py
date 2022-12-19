from src.services.logs.logger import Logger


class JsonUtil(object):
    def __init__(self, json):
        self.json = json

    def get_value(self, param, log=True):
        """Reads the json object and returns the parameter value.
        Log is set to true by default to show the results, but using false the results won't be printed.

        :param param: key value in json response.
        :param log: True to show the logs in terminal
        :return: value: value from key.
        """
        value = None

        try:
            value = self.json[param]

            if log is True:
                Logger(f'{param}: {value}').substep_passed()
        except KeyError:
            Logger(f"param '{param}' from json not found: {self.json}").substep_failed()
        return value
