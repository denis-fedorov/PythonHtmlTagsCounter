from allHtmlTags import tagsList
from bs4 import BeautifulSoup


class TagCounter:
    """
    A class for html-tags counting
    """

    @staticmethod
    def getTags(rawHtml):
        source = str(rawHtml).lower()
        soup = BeautifulSoup(source, "html.parser")
        result = {}

        for tag in tagsList:
            count = len(soup.find_all(tag))
            if count > 0:
                result[tag] = count

        return result
