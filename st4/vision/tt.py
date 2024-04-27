from typing import Optional

from .tag import tag
from .types import ContextBase


class tt(tag):
    """
    Represents the 'tt' (teletype text) HTML tag, which was traditionally used to display text using the monospace
    font similar to what was used on old teletypes and terminals. This tag is useful for displaying computer code or
    other text where fixed-width formatting is advantageous, though it is now considered obsolete in modern web standards
    and replaced largely by the <code> tag.

    Example usage:
        tt(content="This text will appear in a monospace font.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
