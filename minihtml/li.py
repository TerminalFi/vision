from typing import Optional

from .tag import Tag


class li(Tag):
    """
    Represents the 'li' HTML tag, used to define a list item in an ordered (ol) or unordered (ul) list.
    This tag is essential for creating structured lists of items, which can be styled and customized using CSS.
    The 'li' elements are usually contained within parent 'ul' or 'ol' elements to denote list membership.

    Example usage:
        li(content="This is an item in a list.")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
