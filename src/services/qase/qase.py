import json

import requests
from datetime import date



# qase_admin_token = get_secret('qa/qase/token')
from src.services.read_params.json_util import JsonUtil

qase_admin_token = "00fe36d10fca731d326cb9b9b8641970d8fc7355"
qase_project_id = 'IMMFLY'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Token": qase_admin_token,
}

server_id = {"dev": 1,
             "localhost": 2,
             "pre": 3}

current_date = str(date.today().strftime("%d/%m/%Y"))


class Qase:
    def __get_server_id(self, server):
        try:
            return server_id[server]
        except:
            return None

    def publish_test_run(self, environment, server):
        """Creates new test run on qase by API request

        :param environment: Backend, webapp, apps
        :param server: dev, localhost
        :return: test_run_id
        """
        env_id = self.__get_server_id(server)
        title = f"[{environment}] Front end tests - {current_date}"

        payload = json.dumps({
            "title": title,
            "description": "E2E Immfly test cases.",
            "environment_id": env_id,
            "cases": [1]
        })

        response = requests.post(url=f'https://api.qase.io/v1/run/{qase_project_id}',
                                 headers=headers,
                                 data=payload)

        json_response = json.loads(response.text)
        return str(json_response['result']['id'])

    def publish_test_case(self, id_run, id_test, test_result):
        """Publish test case on test run created previously.

        :param id_run: test run id created on publish_test_run
        :param id_test: test id from qase
        :param test_result: passed/failed
        """
        payload = json.dumps({"case_id": id_test,
                              "status": test_result,
                              "comment": "Automated test run"})

        requests.post(url=f'https://api.qase.io/v1/result/{qase_project_id}/{id_run}',
                      headers=headers,
                      data=payload)

    def make_public_results(self, id_run):
        """Create public report

        :param id_run: test run id created on publish_test_run
        """
        payload = json.dumps({"status": True})
        response = requests.patch(f"https://api.qase.io/v1/run/{qase_project_id}/{id_run}/public",
                                  headers=headers,
                                  data=payload)

        result = JsonUtil(response.json()).get_value("result", False)
        url = JsonUtil(result).get_value("url", False)
        return url
