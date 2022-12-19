import yaml


def read_yaml(path):
    """Gets the yaml file and returns all the elements.

    :return: yaml file
    """
    with open(path) as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
