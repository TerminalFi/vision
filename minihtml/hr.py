from .tag import SelfClosingTag


class hr(SelfClosingTag):
    def __init__(self, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
