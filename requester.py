import requests


class Requester:
    """
    A class for sending http-requests
    """

    @staticmethod
    def sendRequest(url):
        try:
            response = requests.get(url)
            return ("ok", response.text)
        except Exception as exp:
            return ("", str(exp))
