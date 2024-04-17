from typing import Union

from .tag import Tag


class h2(Tag):
    """
    Represents the 'h2' HTML tag, used for secondary headings on a web page. This tag is typically used to denote
    subheadings or section titles under the main 'h1' heading, helping to organize content hierarchically and improve
    readability and SEO structure.

    Example usage:
        h2(content="Section Title: Introduction to the Topic")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
