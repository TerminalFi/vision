from .tag import tag
from .types import ContextBase


class ol(tag):
    """
    Represents the 'ol' HTML tag, used to create an ordered list where each list item is automatically numbered.
    This tag is ideal for making lists that require sequential enumeration such as recipes, rankings, or any
    step-by-step instructions.

    Example usage:
        with ol():
            li(content="First item")
            li(content="Second item")
    """

    def __init__(self, ctx: ContextBase, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
