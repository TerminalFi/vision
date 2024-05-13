import html
import re
from typing import Any, Iterable, List, Union

from .renderable import BaseTag
from .style import style
from .text import Text

SELF_CLOSING_TAGS = ["img", "br", "hr", "input", "link", "meta"]

RE_BAD_ENTITIES = re.compile(r"(&(?!amp;|lt;|gt;|nbsp;)(?:\w+;|#\d+;))")


def _remove_entities(text):
    """Remove unsupported HTML entities."""

    def repl(m):
        """Replace entities except &, <, >, and `nbsp`."""
        return html.unescape(m.group(1))

    return RE_BAD_ENTITIES.sub(repl, text)


class tag(BaseTag):
    """
    Extends BaseTag to handle content management and child elements specifically. This class allows for the creation
    of nested HTML structures using context management to maintain a clean layout in the code.

    Example usage:
    with Tag('div') as div:
        div.child(Tag('span', content='Hello'), Tag('span', content='World'))
    """

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._children: List[Union["tag", SelfClosingTag, style, Text]] = []
        self._content: str = ""

    def __enter__(self):
        if self.ctx is not None:
            self._previous_current = self.ctx.current
            self.ctx.push(self)  # type: ignore
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ctx is not None:
            self.ctx.pop(self)

    # Child Handling
    def child(self, *elems: Union["tag", style, Text, Iterable[Union["tag", style, Text]]]):
        with self.ctx._lock:  # type: ignore
            for elem in elems:
                if isinstance(elem, (tag, style, Text)):
                    self._children.append(elem)
                else:
                    self._children.extend(elem)
        return self

    # Content Management
    def content(self, content: str, escape: bool = True) -> "tag":
        if not content:
            return self
        with self.ctx._lock:  # type: ignore
            if escape:
                self._content = _remove_entities(html.escape(content))
            else:
                self._content = content
        return self

    def render(self) -> str:
        """
        Recursively render the element and its children to an HTML string.
        """
        if self._should_render is False:
            return ""

        with self.ctx._lock:  # type: ignore
            # Convert styles dictionary to a style string
            style_str = "; ".join(f"{key}: {value}" for key, value in self._styles.items())
            style_attr = f' style="{style_str}"' if style_str else ""

            # Convert attributes dictionary to an attributes string, excluding class and id as they're handled separately
            attr_str = " ".join(
                f"{key}='{value}'" for key, value in self._attributes.items() if key not in ["id", "class"]
            )

            # Handle id and class attributes specially to ensure they're included
            id_attr = f' id="{self.id}"' if self.id else ""
            class_attr = f' class="{" ".join(self._classes)}"' if self._classes else ""

            # Opening tag with attributes and styles
            open_tag = f"<{self.tag}{id_attr}{class_attr}{style_attr}{' ' + attr_str if attr_str else ''}>"
            if self.tag.lower() in SELF_CLOSING_TAGS:
                return open_tag

        # Recursively render children and concatenate their HTML
        children_html = ""
        for child in self._children:
            if child is None:
                continue
            children_html = f"{children_html}{child.render()}"

        # Closing tag
        close_tag = f"</{self.tag}>"
        # Combine everything
        return f"{open_tag}{self._content}{children_html}{close_tag}"

    # Query Methods
    def query_by_id(self, id_value: str) -> Union["tag", None]:
        """
        Recursively query the element and its children for an element with a specific id, ensuring thread safety.
        """
        with self.ctx._lock:  # type: ignore
            if self.id == id_value:
                return self
            for child in self._children:
                if isinstance(child, (style, Text, SelfClosingTag)):
                    continue
                result = child.query_by_id(id_value)
                if result is not None:
                    return result
            return None

    def query_by_class(self, class_value: str) -> List["tag"]:
        """
        Recursively query the element and its children for elements with a specific class, ensuring thread safety.
        """
        results = []
        if class_value in self._classes:
            results.append(self)
        for child in self._children:
            if isinstance(child, tag):
                additional_results = child.query_by_class(class_value)
                if additional_results:  # Ensure that additional_results is not None and is iterable
                    results.extend(additional_results)
        return results


class SelfClosingTag(BaseTag):
    """
    Represents HTML tags that do not contain content or children, such as <br>, <img>, <hr>. These tags
    are used to perform specific functions on webpages, like inserting a line break or displaying an image,
    without needing to be closed with a separate end tag.

    Raises:
        TypeError: If an attempt is made to add children to a self-closing tag, a TypeError is raised.

    Example:
        # Correct usage
        img_tag = SelfClosingTag('img', src='path/to/image.png')

        # Incorrect usage, raises TypeError
        with SelfClosingTag('br') as br:
            br.child(Tag('span'))  # This will raise an error
    """

    def __init__(self, ctx: Any, tag, *args, **kwargs):
        if tag not in SELF_CLOSING_TAGS:
            raise ValueError(f"{tag} is not a valid self-closing tag")
        super().__init__(ctx, tag, *args, **kwargs)

    def child(self, *elems):
        # Override to prevent any children from being added
        raise TypeError(f"Self-closing tags such as {self.tag} cannot contain children.")

    def render(self):
        """
        Recursively render the element and its children to an HTML string.
        """
        if self._should_render is False:
            return ""

        with self.ctx._lock:  # type: ignore
            # Convert styles dictionary to a style string
            style_str = "; ".join(f"{key}: {value}" for key, value in self._styles.items())
            style_attr = f' style="{style_str}"' if style_str else ""

            # Convert attributes dictionary to an attributes string, excluding class and id as they're handled separately
            attr_str = " ".join(
                f"{key}='{value}'" for key, value in self._attributes.items() if key not in ["id", "class"]
            )

            # Handle id and class attributes specially to ensure they're included
            id_attr = f' id="{self.id}"' if self.id else ""
            class_attr = f' class="{" ".join(self._classes)}"' if self._classes else ""

            # Opening tag with attributes and styles
            open_tag = f"<{self.tag}{id_attr}{class_attr}{style_attr}{' ' + attr_str if attr_str else ''}>"
            if self.tag.lower() in SELF_CLOSING_TAGS:
                return open_tag
