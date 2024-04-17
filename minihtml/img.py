from typing import Union

from .tag import SelfClosingTag


class img(SelfClosingTag):
    def __init__(self, src: Union[str, None], *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if src:
            self.set_attribute("src", src)
