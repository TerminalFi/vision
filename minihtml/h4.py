from .element import element


class h4(element):
    def __init__(self, *args, **kwargs):
        self.tag = self.__class__.__name__
        super().__init__(self.tag, *args, **kwargs)
