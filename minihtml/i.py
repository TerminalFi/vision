from typing import Union

from .tag import Tag


class i(Tag):
    def __init__(self, content: Union[str, None] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
