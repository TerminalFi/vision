from typing import Optional

from .tag import tag
from .types import ContextBase


class em(tag):
    """
    Represents the 'em' HTML tag, which is used to emphasize text. Semantically, it implies that the enclosed text should
    be stressed or given emphasis when read, which is generally reflected by italicizing the text in visual browsers. This
    tag can be useful for altering the tone or mood of text content, subtly differentiating it from surrounding text.

    Example usage:
        emphasized_text = em(content="This text will be emphasized, typically styled in italics.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
