from typing import Optional

from .tag import tag
from .types import ContextBase


class var(tag):
    """
    Represents the 'var' HTML tag, used to define a variable in a mathematical expression or a programming context.
    This tag is typically rendered in italics to signify that the text is a variable name, not regular text. It helps
    to distinguish programmatically relevant terms or mathematical variables from surrounding text, aiding in readability
    and comprehension.

    Example usage:
        with p(content="Let "):
            var(content="x")
            Text(" be the number of apples.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
