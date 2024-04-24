from .context import Context
from .tag import SelfClosingTag


class hr(SelfClosingTag):
    """
    Represents the 'hr' HTML tag, a self-closing element used to create a thematic break between paragraph-level
    elements within an HTML document. It is typically rendered as a horizontal rule (line) and can be used to
    visually separate content such as different topics in a text or different sections on a webpage.

    Example usage:
        hr()
        # Renders as a horizontal line in HTML, visually separating content.
    """

    def __init__(self, ctx: Context, *args, **kwargs):
        super().__init__(ctx, self.__class__.__name__, *args, **kwargs)
