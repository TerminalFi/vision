from typing import Union

from .tag import Tag


class u(Tag):
    """
    Represents the 'u' HTML tag, used to underline text. This tag is primarily used for adding a simple underline styling
    to text without implying any additional semantic meaning like emphasis or importance, which other tags such as <em>
    or <strong> might denote.

    Example usage:
        u(content="This text will be underlined.")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
