from typing import Optional

from .tag import Tag


class small(Tag):
    """
    Represents the 'small' HTML tag, which is used to render text in a smaller font size relative to the surrounding
    elements. This tag is typically used to denote fine print or side comments that are not the main focus of the
    webpage but provide additional information or disclaimers.

    Example usage:
        small(content="This text will appear smaller than normal text to indicate less emphasis.")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
