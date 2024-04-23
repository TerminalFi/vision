from typing import Optional

from .tag import Tag


class h6(Tag):
    """
    Represents the 'h6' HTML tag, which is used for the sixth level of headings in an HTML document. This tag is
    typically used to provide the least emphatic heading level, often for labeling deeply nested sections or
    minor headings within a page.

    Example usage:
        h6(content="Minor Topic Details")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
