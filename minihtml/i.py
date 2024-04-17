from typing import Union

from .tag import Tag


class i(Tag):
    """
    Represents the 'i' HTML tag, which is commonly used to italicize text. This tag provides a way to emphasize text
    stylistically without implying any additional importance or emphasis semantically, unlike the <em> tag which suggests
    emphasis in the meaning of the words.

    Example usage:
        i(content="This text will be rendered in italic style.")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
