from typing import Optional

from .tag import Tag


class big(Tag):
    """
    Represents a 'big' HTML tag, used historically to increase the font size of the enclosed text by one size larger
    than the default text size. It is often used to emphasize text visually without implying additional importance
    which might otherwise be conveyed by stronger emphasis tags like <strong>.

    Example usage:
        big(content="This text will appear slightly larger than surrounding text.")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
