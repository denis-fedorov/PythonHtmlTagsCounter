import re

urlPattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
regex = re.compile(urlPattern)


class Validator:
    """
    A class for an URL address validation
    """
    @staticmethod
    def isurlcorrect(url):
        return re.match(regex, url)
