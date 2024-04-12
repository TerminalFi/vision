from typing import Union

from minihtml.element import renderable


class style(renderable):
    def __init__(self, default_css: Union[dict, None]):
        self.css = default_css or {}
        self.tag = self.__class__.__name__

    def add_css(self, selector: str, properties: dict):
        if selector in self.css:
            self.css[selector].update(properties)
        else:
            self.css[selector] = properties

    def render(self) -> str:
        css_str = ""
        for selector, props in self.css.items():
            props_str = ""
            for key, value in props.items():
                props_str += (
                    f"{key}: {value}; "
                    if not str(value).endswith(";")
                    else f"{key}: {value} "
                )
            props_str.rstrip()
            css_str += f"{selector} {{{props_str}}}\n"
        return f"<{self.tag}>{css_str}</{self.tag}>"
