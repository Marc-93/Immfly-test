from src.shared_utils.aws.secrets import get_secret
from src.shared_utils.logs.logger import Logger


class BrazeData:
    def get_braze_url(self):
        """Gets the braze url from dev environment

        :return: braze dev url
        """
        return "https://rest.braze.eu/"

    def get_braze_token(self, site):
        """Gets the value from specific site to return the Braze token.

        :param site: platform where event is generated
        :return: token for header
        """
        token = ""
        if str(site).lower() == "web":
            token = get_secret('secret_path')
        elif str(site).lower() == "android":
            token = get_secret("secret_path")
        elif str(site).lower() == "ios":
            token = get_secret("dev/braze/ios")
        elif str(site).lower() == "backend":
            token = get_secret("secret_path")
        else:
            Logger("[Braze] Site or key not valid!").substep_failed()

        return f"Bearer {token}"
