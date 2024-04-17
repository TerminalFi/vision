from typing import Union

from .tag import Tag


class strong(Tag):
    """
    Represents the 'strong' HTML tag, which is used to indicate that its contents have strong importance, seriousness, or urgency.
    Browsers typically render the contents in bold type. This tag not only changes the style of the text but also signifies
    importance for accessibility tools and search engines.

    Example usage:
        strong(content="This text is of great importance.")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
