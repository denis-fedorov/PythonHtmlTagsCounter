import requests
from keyValuePair import KeyValuePair


class Requester:
    """
    A class for sending http-requests
    """

    @staticmethod
    def sendRequest(url):
        try:
            response = requests.get(url)
            return KeyValuePair("ok", response.text)
        except requests.exceptions.ConnectionError as exp:
            return KeyValuePair("", "Invalid URL")
        except Exception as exp:
            return KeyValuePair("", str(exp))
