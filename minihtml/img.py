from .element import element


class img(element):
    def __init__(self, src: str, content: str, *args, **kwargs):
        self.tag = self.__class__.__name__
        super().__init__(self.tag, *args, **kwargs)
        self.set_attribute("src", src)
        self.add_content(content)
