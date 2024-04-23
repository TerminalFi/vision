from typing import Optional

from .tag import Tag


class h3(Tag):
    """
    Represents the 'h3' HTML tag, used for tertiary headings within web content. This tag is commonly used to define
    sub-sections within a larger section marked by 'h2' tags, aiding in the structural organization of the page and
    enhancing SEO by providing clear hierarchical levels in the document.

    Example usage:
        h3(content="Detailed Analysis of the Topic")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
