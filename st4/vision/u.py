from typing import Optional

from .tag import tag
from .types import ContextBase


class u(tag):
    """
    Represents the 'u' HTML tag, used to underline text. This tag is primarily used for adding a simple underline styling
    to text without implying any additional semantic meaning like emphasis or importance, which other tags such as <em>
    or <strong> might denote.

    Example usage:
        u(content="This text will be underlined.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
