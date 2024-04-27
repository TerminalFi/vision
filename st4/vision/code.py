from typing import Optional

from .tag import tag
from .types import ContextBase


class code(tag):
    """
    Represents the 'code' HTML tag, used to display a segment of computer code. By default, content within a 'code' tag
    is displayed in the browser's default monospace font.

    Example usage:
        code(content="border-radius")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)

        if content:
            self.content(content)


# type: ignore
