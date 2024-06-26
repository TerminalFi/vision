from typing import Optional

from .tag import tag
from .types import ContextBase


class body(tag):
    """
    Represents the 'body' HTML tag, which encloses the main content of an HTML document. This tag is used as a container
    for all the contents of an HTML document except for the head tag, typically including text, hyperlinks, images, tables,
    and lists.

    Example usage:
        main_content = body()
        main_content.child(p(content="This is a paragraph in the body of the document."))
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
