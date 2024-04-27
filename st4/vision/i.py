from typing import Optional

from .tag import tag
from .types import ContextBase


class i(tag):
    """
    Represents the 'i' HTML tag, which is commonly used to italicize text. This tag provides a way to emphasize text
    stylistically without implying any additional importance or emphasis semantically, unlike the <em> tag which suggests
    emphasis in the meaning of the words.

    Example usage:
        i(content="This text will be rendered in italic style.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
