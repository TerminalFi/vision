from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Set

import sublime


class AllowedTags(Enum):
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


@dataclass(frozen=True)
class Tag:
    name: AllowedTags


@dataclass
class TagValidator:
    allowed_tags: Set[AllowedTags] = field(default_factory=set)

    def add_tag(self, tag: AllowedTags):
        """Adds a new tag to the set of allowed tags"""
        self.allowed_tags.add(tag)

    def is_valid_tag(self, tag_name: str) -> bool:
        """Checks if a tag is in the allowed set"""
        return AllowedTags(tag_name) in self.allowed_tags


tag_validator = TagValidator()
[tag_validator.add_tag(tag) for tag in AllowedTags]


class AllowedAttributes(Enum):
    HREF = "href"
    ID = "id"
    CLASS = "class"
    TITLE = "title"


@dataclass(frozen=True)
class Attribute:
    name: str
    allowed_values: Optional[frozenset] = field(default_factory=frozenset)

    def validate(self, value: str) -> bool:
        if self.allowed_values is None or len(self.allowed_values) == 0 or value in self.allowed_values:
            return True
        else:
            raise ValueError(
                f"Value '{value}' is not allowed for property '{self.name}'. "
                + f"Allowed values are: {self.allowed_values}"
            )

    def validate_href(self, value: str) -> bool:
        if value.startswith("https://") or value.startswith("http://") or value.startswith("subl:"):
            return True
        else:
            raise ValueError(
                f"Value '{value}' is not allowed for property '{self.name}'. "
                + f"Allowed values are: {self.allowed_values}"
            )


@dataclass
class AttributeValidator:
    attributes: Set[Attribute] = field(default_factory=set)

    def add_attribute(self, property: Attribute):
        self.attributes.add(property)

    def validate(self, attribute_name: str, value: str) -> bool:
        for attrib in self.attributes:
            if attrib.name == attribute_name:
                if attrib.name == AllowedAttributes.HREF.value:
                    return attrib.validate_href(value)
                else:
                    return attrib.validate(value)
        raise ValueError(f"Attribute '{attribute_name}' is not supported.")


attribute_validator = AttributeValidator()
attribute_validator.add_attribute(Attribute(AllowedAttributes.HREF.value, frozenset(["https://", "http://", "subl:"])))
attribute_validator.add_attribute(Attribute(AllowedAttributes.CLASS.value))
attribute_validator.add_attribute(Attribute(AllowedAttributes.ID.value))
attribute_validator.add_attribute(Attribute(AllowedAttributes.TITLE.value))


@dataclass(frozen=True)
class CSSProperty:
    name: str
    allowed_values: Optional[frozenset] = field(default_factory=frozenset)

    def validate(self, value: str) -> bool:
        if self.allowed_values is None or len(self.allowed_values) == 0 or value in self.allowed_values:
            return True
        else:
            raise ValueError(
                f"Value '{value}' is not allowed for property '{self.name}'. "
                + f"Allowed values are: {self.allowed_values}"
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
css_validator.add_property(CSSProperty("border-top-right-radius"))
css_validator.add_property(CSSProperty("border-top-left-radius"))
css_validator.add_property(CSSProperty("border-bottom-right-radius"))
css_validator.add_property(CSSProperty("border-bottom-left-radius"))
css_validator.add_property(CSSProperty("border-right"))
css_validator.add_property(CSSProperty("border-style"))
css_validator.add_property(CSSProperty("border-top"))
css_validator.add_property(CSSProperty("border-width"))
css_validator.add_property(CSSProperty("bottom"))
css_validator.add_property(CSSProperty("color"))
if sublime.version() >= "4085":
    css_validator.add_property(
        CSSProperty("display", frozenset(["none", "block", "inline", "inline-block", "list-item"]))
    )
else:
    css_validator.add_property(CSSProperty("display", frozenset(["none", "block", "inline", "list-item"])))

css_validator.add_property(CSSProperty("font-family"))
css_validator.add_property(CSSProperty("font-size"))
css_validator.add_property(CSSProperty("font-style", frozenset(["normal", "italic"])))
css_validator.add_property(CSSProperty("font-weight", frozenset(["normal", "bold"])))
css_validator.add_property(CSSProperty("height"))
css_validator.add_property(CSSProperty("left"))
css_validator.add_property(CSSProperty("line-height"))
css_validator.add_property(CSSProperty("list-style-type", frozenset(["circle", "disc", "square"])))
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
css_validator.add_property(CSSProperty("position", frozenset(["relative", "static"])))
css_validator.add_property(CSSProperty("right"))
css_validator.add_property(CSSProperty("text-align", frozenset(["left", "right", "center"])))
css_validator.add_property(CSSProperty("text-decoration", frozenset(["none", "underline"])))
css_validator.add_property(CSSProperty("top"))
if sublime.version() >= "4173":
    css_validator.add_property(CSSProperty("white-space", frozenset(["normal", "nowrap", "pre", "pre-wrap"])))
else:
    css_validator.add_property(CSSProperty("white-space", frozenset(["normal", "nowrap"])))
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
