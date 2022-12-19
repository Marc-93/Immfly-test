import time
from dataclasses import dataclass

import requests

from src.services.logs.logger import Logger


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class ApiRequest:
    def get(self, url, headers=None, params=None, log=""):
        """Performs a get request.

        :param url: host + api path
        :param headers: json headers
        :param params: url params
        :param log: log text
        :return: json response
        """
        response = requests.get(url, headers=headers, params=params)
        return self.__get_responses(response, log)

    def post(self, url, payload, headers=None, log="", file=None):
        """Performs a post request.

        :param url: host + api path
        :param payload: json body
        :param headers: json headers
        :param log: log text
        :return: json response
        """
        if file == None:
            response = requests.post(url, data=payload, headers=headers)
        else:
            response = requests.post(url, data=payload, headers=headers, files=file)
        return self.__get_responses(response, log)


    def patch(self, url, payload, headers=None, log=""):
        """Performs a patch request.

        :param url: host + api path
        :param payload: json body
        :param headers: json headers
        :param log: log text
        :return: json response
        """
        response = requests.patch(url, data=payload, headers=headers)
        return self.__get_responses(response, log)

    def put(self, url, payload, headers=None, log=""):
        """Performs a patch request.

        :param url: host + api path
        :param payload: json body
        :param headers: json headers
        :param log: log text
        :return: json response
        """
        response = requests.put(url, data=payload, headers=headers)
        return self.__get_responses(response, log)

    def delete(self, url, headers=None, data=None, log=""):
        """Performs a delete request.

        :param url: host + api path
        :param headers: json headers
        :param log: log text
        :return: json response
        """
        try:
            payload = {}
            if data != None:
                payload = data

            response = requests.delete(url, headers=headers, data=payload)
            if log != "":
                Logger(f"[Request] {log} - status: {response.status_code} - reason: {response.reason}").substep_passed()
            else:
                Logger(f"[Request] status: {response.status_code}").substep_passed()
        except:
            Logger(f"[Delete] Error while deleting data").substep_failed()

    def __get_responses(self, response, log=""):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
            if log != "":
                Logger(f"[Request] {log} - status: {response.status_code} - reason: {response.reason}").substep_passed()
            else:
                Logger(f"[Request] status: {response.status_code}").substep_passed()
            time.sleep(0.3)

        except:
            as_dict = None
            Logger(f'status code: {response.status_code}').substep_passed()
            Logger(f'reason: {response.reason}').substep_passed()
            Logger(f'url: {response.url}').substep_passed()

        headers = response.headers
        return Response(status_code, text, as_dict, headers)
