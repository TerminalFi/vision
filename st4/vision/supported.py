from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Set

import sublime


class Tags(Enum):
    A = "a"
    B = "b"
    BIG = "big"
    BODY = "body"
    BR = "br"
    CODE = "code"
    DIV = "div"
    EM = "em"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    HEAD = "head"
    HR = "hr"
    I = "i"
    IMG = "img"
    LI = "li"
    OL = "ol"
    P = "p"
    SMALL = "small"
    SPAN = "span"
    STRONG = "strong"
    STYLE = "style"
    TAG = "tag"
    TT = "tt"
    U = "u"
    UL = "ul"
    VAR = "var"


class Attributes(Enum):
    HREF = "href"
    ID = "id"
    CLASS = "class"
    TITLE = "title"


@dataclass
@dataclass(frozen=True)
class CSSProperty:
    name: str
    allowed_values: Optional[Set[str]] = field(default=None)

    def validate(self, value: str) -> bool:
        if self.allowed_values is None or value in self.allowed_values:
            return True
        else:
            raise ValueError(
                f"Value '{value}' is not allowed for property '{self.name}'. "
                f"Allowed values are: {self.allowed_values}"
            )


@dataclass
class CSSValidator:
    properties: Set[CSSProperty] = field(default_factory=set)

    def add_property(self, property: CSSProperty):
        self.properties.add(property)

    def validate(self, property_name: str, value: str) -> bool:
        for prop in self.properties:
            if prop.name == property_name:
                return prop.validate(value)
        raise ValueError(f"CSS property '{property_name}' is not supported.")


css_validator = CSSValidator()
css_validator.add_property(CSSProperty("background-color"))
css_validator.add_property(CSSProperty("border"))
css_validator.add_property(CSSProperty("border-bottom"))
css_validator.add_property(CSSProperty("border-color"))
css_validator.add_property(CSSProperty("border-left"))
css_validator.add_property(CSSProperty("border-radius"))
css_validator.add_property(CSSProperty("border-right"))
css_validator.add_property(CSSProperty("border-style"))
css_validator.add_property(CSSProperty("border-top"))
css_validator.add_property(CSSProperty("border-width"))
css_validator.add_property(CSSProperty("bottom"))
css_validator.add_property(CSSProperty("color"))
if sublime.version() >= "4085":
    css_validator.add_property(CSSProperty("display", {"none", "block", "inline", "inline-block", "list-item"}))
else:
    css_validator.add_property(CSSProperty("display", {"none", "block", "inline", "list-item"}))

css_validator.add_property(CSSProperty("font-family"))
css_validator.add_property(CSSProperty("font-size"))
css_validator.add_property(CSSProperty("font-style", {"normal", "italic"}))
css_validator.add_property(CSSProperty("font-weight", {"normal", "bold"}))
css_validator.add_property(CSSProperty("height"))
css_validator.add_property(CSSProperty("left"))
css_validator.add_property(CSSProperty("line-height"))
css_validator.add_property(CSSProperty("list-style-type", {"circle", "disc", "square"}))
css_validator.add_property(CSSProperty("margin"))
css_validator.add_property(CSSProperty("margin-bottom"))
css_validator.add_property(CSSProperty("margin-left"))
css_validator.add_property(CSSProperty("margin-right"))
css_validator.add_property(CSSProperty("margin-top"))
css_validator.add_property(CSSProperty("padding"))
css_validator.add_property(CSSProperty("padding-bottom"))
css_validator.add_property(CSSProperty("padding-left"))
css_validator.add_property(CSSProperty("padding-right"))
css_validator.add_property(CSSProperty("padding-top"))
css_validator.add_property(CSSProperty("position", {"relative", "static"}))
css_validator.add_property(CSSProperty("right"))
css_validator.add_property(CSSProperty("text-align", {"left", "right", "center"}))
css_validator.add_property(CSSProperty("text-decoration", {"none", "underline"}))
css_validator.add_property(CSSProperty("top"))
if sublime.version() >= "4173":
    css_validator.add_property(CSSProperty("white-space", {"normal", "nowrap", "pre", "pre-wrap"}))
else:
    css_validator.add_property(CSSProperty("white-space", {"normal", "nowrap"}))
css_validator.add_property(CSSProperty("width"))


class CSSProperties(Enum):
    BACKGROUND_COLOR = ("background-color", None)
    BORDER = ("border", None)
    BORDER_BOTTOM = ("border-bottom", None)
    BORDER_COLOR = ("border-color", None)
    BORDER_LEFT = ("border-left", None)
    BORDER_RADIUS = ("border-radius", None)
    BORDER_RIGHT = ("border-right", None)
    BORDER_STYLE = ("border-style", None)
    BORDER_TOP = ("border-top", None)
    BORDER_WIDTH = ("border-width", None)
    BOTTOM = ("bottom", None)
    COLOR = ("color", None)
    DISPLAY = ("display", None)
    FONT_FAMILY = ("font-family", None)
    FONT_SIZE = ("font-size", None)
    FONT_STYLE = ("font-style", None)
    FONT_WEIGHT = ("font-weight", None)
    HEIGHT = ("height", None)
    LEFT = ("left", None)
    LINE_HEIGHT = ("line-height", None)
    LIST_STYLE_TYPE = ("list-style-type", None)
    MARGIN = ("margin", None)
    MARGIN_BOTTOM = ("margin-bottom", None)
    MARGIN_LEFT = ("margin-left", None)
    MARGIN_RIGHT = ("margin-right", None)
    MARGIN_TOP = ("margin-top", None)
    PADDING = ("padding", None)
    PADDING_BOTTOM = ("padding-bottom", None)
    PADDING_LEFT = ("padding-left", None)
    PADDING_RIGHT = ("padding-right", None)
    PADDING_TOP = ("padding-top", None)
    POSITION = ("position", None)
    RIGHT = ("right", None)
    TEXT_ALIGN = ("text-align", None)
    TEXT_DECORATION = ("text-decoration", None)
    TOP = ("top", None)
    WHITE_SPACE = ("white-space", None)
    WIDTH = ("width", None)
