from typing import Union

from .tag import Tag


class h1(Tag):
    """
    Represents the 'h1' HTML tag, typically used for the main heading of a page. This tag is important for SEO as it
    helps to define the primary subject matter of the web page content. Text within 'h1' is usually displayed in the
    largest font size by default, emphasizing its importance as the top-level heading in the document structure.

    Example usage:
        h1(content="Welcome to My Web Page")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
