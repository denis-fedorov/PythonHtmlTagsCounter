import requests
from utils.keyValuePair import key_value_pair


class Requester:
    """
    A class for sending http-requests
    """
    @staticmethod
    def send_request(url):
        try:
            response = requests.get(url)
            return key_value_pair("ok", response.text)
        except requests.exceptions.ConnectionError:
            return key_value_pair("", "Invalid URL")
        except Exception as exp:
            return key_value_pair("", str(exp))
