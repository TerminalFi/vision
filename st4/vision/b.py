from typing import Optional

from .types import ContextBase
from .tag import tag


class b(tag):
    """
    Represents a bold text tag (<b>) in HTML, used to make text bold without conveying any additional importance.
    This class extends the Tag class and can be used to encapsulate text in a bold style purely for visual enhancement.

    Example usage:
        b(content="This is bold text")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
