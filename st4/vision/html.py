from .tag import tag
from .types import ContextBase


class html(tag):
    """
    Represents an anchor tag (<a>) in HTML, used to create hyperlinks on web pages. This class allows for the dynamic setting
    of the 'href' attribute and the content of the anchor tag, facilitating the creation of clickable links that can navigate
    to different URLs or trigger actions.

    Attributes:
        href (str): The URL the hyperlink points to.
        content (str): The text or HTML to be displayed as part of the hyperlink.

    Example usage:
        html()
    """

    def __init__(self, ctx: ContextBase, content: str, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
