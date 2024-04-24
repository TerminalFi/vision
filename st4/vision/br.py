from .context import Context
from .tag import SelfClosingTag


class br(SelfClosingTag):
    """
    Represents the 'br' HTML tag, a self-closing element used to insert a line break in the text. It is commonly used
    to break lines of text or add spacing between lines without starting a new paragraph, which would have additional
    margins or padding.

    Example usage:
        # Inserts a line break between two lines of text within the same paragraph
        p(content="This is the first line")
        br()
        p(content="second line after break")
    """

    def __init__(self, ctx: Context, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
