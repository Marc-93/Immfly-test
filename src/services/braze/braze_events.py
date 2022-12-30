from datetime import date

from src.shared_utils.braze.braze_data import BrazeData
from src.shared_utils.logs.logger import Logger
from src.shared_utils.api.api_request import ApiRequest


def get_braze_event_list(event_name, event_origin, server_name="test"):
    """Executes a braze request to get the current data about number of times that event is executed by today.

    :param event_name: event id
    :param server_name: server site
    :param event_origin: site that triggers the event
    """
    # Checks the server, braze just now is only reading data from dev
    if server_name != "test":
        Logger(f"[Server] Braze cannot be executed in {server_name}, try to execute the test in dev.").substep_failed()

    today = str(date.today().strftime("%d/%m/%Y"))

    # Gets the token for specific braze section where event is created and stored.
    braze_token = BrazeData().get_braze_token(event_origin)

    # Creates the url with params
    url = f"{BrazeData().get_braze_url()}events/data_series?event={event_name}&length=1&unit=day&ending_at={today}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': braze_token
    }

    # Executes the request to get the braze event counter for the current day.
    response = ApiRequest().get(url=url,
                                headers=headers,
                                log="Get braze event")

    return response.as_dict['data']
