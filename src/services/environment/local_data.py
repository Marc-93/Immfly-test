import subprocess

from src.services.logs.formatted_print import FormattedPrint
from src.services.read_params.yaml_util import read_yaml


def get_current_user():
    """Gets the current macOS user

    :return: user
    """
    current_path = subprocess.getoutput('pwd').split('/')
    return current_path[2]


class UserLocalData:
    def __init__(self):
        self.user = get_current_user()
        self.yaml_path = 'src/services/environment/local_data.yaml'

    def get_local_data(self, key):
        """Gets the value from specific key that is stored in configuration file

        :param key: param related with server
        :return: value for specific server
        """
        try:
            return read_yaml(self.yaml_path)[key][self.user]
        except:
            FormattedPrint("YAML", "DATA not found in yaml file for current user").pink()
            exit()
