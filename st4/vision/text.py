from .renderable import BaseTag


class Text(BaseTag):
    """
    Represents plain text within an HTML document, encapsulated as a 'Text' object. This class does not correspond to any
    specific HTML tag but is used for inserting raw text into the HTML structure. It does not support nesting (i.e., cannot
    contain child elements), making it suitable for adding unstyled text.

    Example usage:
        Text("This is some plain text.")
    """

    def __init__(self, content: str):
        self._content = content

    def child(self, *elems):
        # Override to prevent any children from being added
        raise TypeError("Text cannot contain children.")

    def render(self):
        return self._content
