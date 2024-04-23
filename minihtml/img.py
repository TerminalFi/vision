from typing import Optional

from .tag import SelfClosingTag


class img(SelfClosingTag):
    """
    Represents the 'img' HTML tag, a self-closing element used to embed an image into a webpage.
    This tag requires a source URL specified via the 'src' attribute to function correctly and may
    include an 'alt' attribute to provide alternative text which describes the image if it cannot be displayed.

    Example usage:
        image = img()
        image.set_attribute("src", "path/to/image.jpg")
        image.set_attribute("alt", "Description of the image")
    """

    def __init__(self, src: Optional[str], *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if src:
            self.set_attribute("src", src)
