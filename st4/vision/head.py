from typing import Optional

from .tag import tag
from .types import ContextBase


class head(tag):
    """
    Represents the 'head' HTML tag, which is used to define the head section of an HTML document.
    This section is a container for metadata (data about data) and is placed between the <html> tag
    and the <body> tag. It includes elements like title, style, meta, link, script, and others that
    help define the document's properties and links to scripts and stylesheets.

    Example usage:
        with head():
            title(content="Example Page Title")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(content, ctx, self.__class__.__name__, *args, **kwargs)
