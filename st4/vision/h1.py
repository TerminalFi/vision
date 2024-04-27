from typing import Optional

from .tag import tag
from .types import ContextBase


class h1(tag):
    """
    Represents the 'h1' HTML tag, typically used for the main heading of a page. This tag is important for SEO as it
    helps to define the primary subject matter of the web page content. Text within 'h1' is usually displayed in the
    largest font size by default, emphasizing its importance as the top-level heading in the document structure.

    Example usage:
        h1(content="Welcome to My Web Page")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
