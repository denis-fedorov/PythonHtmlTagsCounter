import requests
from keyValuePair import KeyValuePair


class Requester:
    """
    A class for sending http-requests
    """
    @staticmethod
    def send_request(url):
        try:
            response = requests.get(url)
            return KeyValuePair("ok", response.text)
        except requests.exceptions.ConnectionError:
            return KeyValuePair("", "Invalid URL")
        except Exception as exp:
            return KeyValuePair("", str(exp))
