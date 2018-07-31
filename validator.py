import re

url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
regex = re.compile(url_pattern)


class Validator:
    """
    A class for an URL address validation
    """
    @staticmethod
    def is_url_correct(url):
        return re.match(regex, url)
