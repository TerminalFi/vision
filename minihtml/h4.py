from typing import Union

from .tag import Tag


class h4(Tag):
    """
    Represents the 'h4' HTML tag, used for quaternary headings on a web page. The 'h4' tag is typically utilized to
    introduce further subdivisions within the sections delineated by 'h3' tags. It plays a crucial role in the
    document outline and helps to clarify the organization of content for both users and search engines.

    Example usage:
        h4(content="Subsection Title: Additional Details")
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
