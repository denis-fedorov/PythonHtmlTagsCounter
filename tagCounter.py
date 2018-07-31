from utils.allHtmlTags import tags_list
from bs4 import BeautifulSoup


class TagCounter:
    """
    A class for html-tags counting
    """
    @staticmethod
    def get_tags(raw_html):
        source = str(raw_html).lower()
        soup = BeautifulSoup(source, "html.parser")
        result = {}

        for tag in tags_list:
            count = len(soup.find_all(tag))
            if count > 0:
                result[tag] = count

        return result
