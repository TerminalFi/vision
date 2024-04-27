from .tag import tag
from .types import ContextBase


class ul(tag):
    """
    Represents the 'ul' HTML tag, used to create an unordered list, typically rendered with bullet points.
    This tag is essential for grouping a collection of items that do not have a specific ordering, making it
    perfect for lists such as shopping lists, to-do lists, or any list where order does not matter.

    Example usage:
        with ul():
            li(content="First item")
            li(content="Second item")
    """

    def __init__(self, ctx: ContextBase, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
