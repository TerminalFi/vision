from typing import Optional

from .tag import tag
from .types import ContextBase


class span(tag):
    """
    Represents the 'span' HTML tag, used for grouping inline-elements in a document. It serves as a container for styling
    purposes without introducing any semantic meaning or changing the document structure. It is versatile for applying
    styles or classes to a part of a text or a subgroup of inline elements.

    Example usage:
        span(content="This text is inside a span.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
