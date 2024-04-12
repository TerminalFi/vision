from enum import Enum
from typing import Any, Callable, Dict, List, Union

from .renderable import Renderable
from .style import style

SELF_CLOSING_TAGS = ["img", "br", "hr", "input", "link", "meta"]


class element(Renderable):
    """
    The element class is a representation of an HTML element. It can be used to generate HTML strings by chaining methods.
    """

    def __init__(
        self,
        tag: str,
        id: Union[str, None] = None,
        classes: Union[List[str], None] = None,
    ):
        self.tag = tag
        self.id = id
        self.classes = classes if classes is not None else []
        self.styles: Dict[str, str] = {}
        self.attributes: Dict[str, str] = {}
        self.content: str = ""
        self.children: List[Union[element, style, str]] = []
        self._should_render = True

    def query_by_id(self, id_value: str) -> Union["element", None]:
        """
        Recursively query the element and its children for an element with a specific id.
        """
        if self.id == id_value:
            return self
        for child in self.children:
            if isinstance(child, (style, str)):
                continue
            result = child.query_by_id(id_value)
            if result is not None:
                return result
        return None

    def query_by_class(self, class_value: str) -> List["element"]:
        """
        Recursively query the element and its children for elements with a specific class.
        """
        results = []
        if class_value in self.classes:
            results.append(self)
        for child in self.children:
            if isinstance(child, (style, str)):
                continue
            results.extend(child.query_by_class(class_value))
        return results

    def render(self) -> str:
        """
        Recursively render the element and its children to an HTML string.
        """
        if self._should_render is False:
            return ""
        # Convert styles dictionary to a style string
        style_str = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
        style_attr = f' style="{style_str}"' if style_str else ""

        # Convert attributes dictionary to an attributes string, excluding class and id as they're handled separately
        attr_str = " ".join(
            f"{key}='{value}'"
            for key, value in self.attributes.items()
            if key not in ["id", "class"]
        )

        # Handle id and class attributes specially to ensure they're included
        id_attr = f' id="{self.id}"' if self.id else ""
        class_attr = f' class="{" ".join(self.classes)}"' if self.classes else ""

        # Opening tag with attributes and styles
        open_tag = f"<{self.tag}{id_attr}{class_attr}{style_attr}{' ' + attr_str if attr_str else ''}>"
        if self.tag.lower() in SELF_CLOSING_TAGS:
            return open_tag

        # Recursively render children and concatenate their HTML
        children_html = "".join(
            child.render() if isinstance(child, (element, style, Renderable)) else child
            for child in self.children
        )

        # Closing tag
        close_tag = f"</{self.tag}>"

        # Combine everything
        return f"{open_tag}{self.content}{children_html}{close_tag}"

    def when(self, condition: Any) -> Any:
        """
        Return self if the condition is True, otherwise set the _should_render flag to False and return self.
        """
        if condition:
            return self
        else:
            self._should_render = False
            return self

    def when_or_else(
        self,
        condition: Any,
        func: Callable[[], Any],
        func_else: Callable[[], Any],
    ) -> List[Any]:
        """
        Return the result of func if the condition is True, otherwise return the result of func_else.
        Useful for adding multiple elements based on a condition.
        """
        if condition:
            return func()
        else:
            return func_else()

    def add_child(self, child: Union["element", style, str]) -> "element":
        """
        Add a child element to the element. If the child is an element and has an id, check if it's unique.
        """
        if isinstance(child, element):
            if child.id is not None and self.query_by_id(child.id) is not None:
                raise ValueError(f"Duplicate id '{child.id}' found in element")
        self.children.append(child)
        return self

    def add_children(self, *children: Union["element", style, str]) -> "element":
        """
        Add multiple child elements to the element.
        """
        for child in children:
            self.add_child(child)
        return self

    def add_content(self, content: str) -> "element":
        self.content += content
        return self

    def set_style(self, key: str, value: str) -> "element":
        self.styles[key] = value
        return self

    def set_attribute(self, key: str, value: str) -> "element":
        self.attributes[key] = value
        return self

    def href(self, value: str) -> "element":
        if self.tag != "a":
            raise ValueError("href is only available for <a> tags")
        self.attributes["href"] = value
        return self

    def br(self) -> "element":
        self.content += "<br>"
        return self

    def width(self, value: str) -> "element":
        self.styles["width"] = value
        return self

    def height(self, value: str) -> "element":
        self.styles["height"] = value
        return self

    def bg_color(self, color: str) -> "element":
        return self.set_style("background-color", color)

    def white_space(self, whitespace_type: str) -> "element":
        return self.set_style("white-space", whitespace_type)

    def white_space_normal(self) -> "element":
        return self.set_style("white-space", "normal")

    def white_space_no_wrap(self) -> "element":
        return self.set_style("white-space", "nowrap")

    def white_space_pre(self) -> "element":
        return self.set_style("white-space", "pre")

    def white_space_pre_wrap(self) -> "element":
        return self.set_style("white-space", "pre-wrap")

    # Display and Position Utilities
    def display(self, display_type) -> "element":
        return self.set_style("display", display_type)

    def display_none(self) -> "element":
        return self.set_style("display", "none")

    def display_inline(self) -> "element":
        return self.set_style("display", "inline")

    def display_block(self) -> "element":
        return self.set_style("display", "block")

    def display_list_item(self) -> "element":
        return self.set_style("display", "list-item")

    def display_inline_block(self) -> "element":
        return self.set_style("display", "inline-block")

    def position(self, position_type: str) -> "element":
        return self.set_style("position", position_type)

    def position_static(self) -> "element":
        return self.set_style("position", "static")

    def position_relative(self) -> "element":
        return self.set_style("position", "relative")

    def top(self, value: str) -> "element":
        return self.set_style("top", value)

    def right(self, value: str) -> "element":
        return self.set_style("right", value)

    def bottom(self, value: str) -> "element":
        return self.set_style("bottom", value)

    def left(self, value: str) -> "element":
        return self.set_style("left", value)

    # Margin Utilities
    def m(self, value: str) -> "element":
        return self.set_style("margin", value)

    def ml(self, value: str) -> "element":
        return self.set_style("margin-left", value)

    def mr(self, value: str) -> "element":
        return self.set_style("margin-right", value)

    def mt(self, value: str) -> "element":
        return self.set_style("margin-top", value)

    def mb(self, value: str) -> "element":
        return self.set_style("margin-bottom", value)

    # Padding Utilities
    def p(self, value: str) -> "element":
        return self.set_style("padding", value)

    def pl(self, value: str) -> "element":
        return self.set_style("padding-left", value)

    def pr(self, value: str) -> "element":
        return self.set_style("padding-right", value)

    def pt(self, value: str) -> "element":
        return self.set_style("padding-top", value)

    def pb(self, value: str) -> "element":
        return self.set_style("padding-bottom", value)

    def px(self, value: str) -> "element":
        return self.pl(value).pr(value)

    def py(self, value: str) -> "element":
        return self.pt(value).pb(value)

    # Border Utilities
    def border(self, width="1px", style="solid", color="black") -> "element":
        return self.set_style("border", f"{width} {style} {color}")

    def border_left(self, width="1px", style="solid", color="black") -> "element":
        return self.set_style("border-left", f"{width} {style} {color}")

    def border_right(self, width="1px", style="solid", color="black") -> "element":
        return self.set_style("border-right", f"{width} {style} {color}")

    def border_top(self, width="1px", style="solid", color="black") -> "element":
        return self.set_style("border-top", f"{width} {style} {color}")

    def border_bottom(self, width="1px", style="solid", color="black") -> "element":
        return self.set_style("border-bottom", f"{width} {style} {color}")

    def border_radius(self, radius: str) -> "element":
        return self.set_style("border-radius", radius)

    def border_top_left_radius(self, radius: str) -> "element":
        return self.set_style("border-top-left-radius", radius)

    def border_top_right_radius(self, radius: str) -> "element":
        return self.set_style("border-top-right-radius", radius)

    def border_bottom_right_radius(self, radius: str) -> "element":
        return self.set_style("border-bottom-right-radius", radius)

    def border_bottom_left_radius(self, radius: str) -> "element":
        return self.set_style("border-bottom-left-radius", radius)

    # Text and Font Styling
    def font_family(self, *family: str) -> "element":
        return self.set_style("font-family", ", ".join(family))

    def font_light(self) -> "element":
        return self.set_style("font-weight", "300")

    def font_medium(self) -> "element":
        return self.set_style("font-weight", "500")

    def font_bold(self) -> "element":
        return self.set_style("font-weight", "700")

    def text_align(self, align: str) -> "element":
        return self.set_style("text-align", align)

    def text_decoration(self, value: str) -> "element":
        return self.set_style("text-decoration", value)

    def text_decoration_none(self) -> "element":
        return self.set_style("text-decoration", "none")

    def text_decoration_underline(self) -> "element":
        return self.set_style("text-decoration", "underline")

    def color(self, color: str) -> "element":
        return self.set_style("color", color)


class Mode(Enum):
    Overwrite = 1
    Append = 2
