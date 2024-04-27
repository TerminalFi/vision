from typing import Optional

from .tag import tag
from .types import ContextBase


class p(tag):
    """
    Represents the 'p' HTML tag, which is used to define a paragraph in a webpage. This tag automatically handles text
    formatting to distinguish paragraphs from other blocks of text by adding a vertical space before and after the
    paragraph content. It is a block-level element used extensively in HTML for structuring textual content.

    Example usage:
        p(content="This is a paragraph that will be separated from other text blocks on the webpage.")
    """

    def __init__(self, ctx: ContextBase, content: Optional[str] = None, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
        if content:
            # check if escape is in args or kwargs

            escape = kwargs.get("escape", True)
            self.content(content, escape)
