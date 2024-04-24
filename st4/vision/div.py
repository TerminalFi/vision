from typing import Optional

from .context import Context
from .tag import Tag


class div(Tag):
    """
    Represents the 'div' HTML tag, widely used as a container for other HTML elements. The 'div' tag is used to group
    blocks of content and layout elements together in sections. It is often styled with CSS to manage layout and
    formatting both for visual presentation and web design structure.

    Example usage:
        with div():
            p(content="This paragraph is inside a 'div' element.")
    """

    def __init__(self, ctx: Context, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
