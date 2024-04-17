from typing import Union

import mdpopups
import sublime

from .tag import Tag


class code(Tag):
    """
    Represents the 'code' HTML tag, used to display a segment of computer code. By default, content within a 'code' tag
    is displayed in the browser's default monospace font. This tag is ideal for marking up programming code snippets
    within technical documentation or discussion forums.

    Example usage:
        code(content="```py\n\nprint('Hello, World!')```")
        # Renders as: <code>print('Hello, World!')</code> in HTML
    """

    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            window = sublime.active_window()
            if not window:
                self.content(content)
            view = window.active_view()
            if not view:
                self.content(content)

            self.content(mdpopups.md2html(view, content))

