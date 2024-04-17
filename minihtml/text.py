from .renderable import BaseTag


class Text(BaseTag):
    def __init__(self, content: str):
        self._content = content

    def child(self, *elems):
        # Override to prevent any children from being added
        raise TypeError("Text cannot contain children.")

    def render(self):
        return self._content
