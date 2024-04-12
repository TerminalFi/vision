from .element import element


class a(element):
    def __init__(self, href: str, content: str, *args, **kwargs):
        self.tag = self.__class__.__name__
        super().__init__(self.tag, *args, **kwargs)
        self.set_attribute("href", href)
        self.add_content(content)
