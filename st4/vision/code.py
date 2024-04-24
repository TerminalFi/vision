from typing import Optional


from .tag import Tag


class code(Tag):
    """
    Represents the 'code' HTML tag, used to display a segment of computer code. By default, content within a 'code' tag
    is displayed in the browser's default monospace font.

    Example usage:
        code(content="border-radius")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)

        if content:
            self.content(content)


# type: ignore
