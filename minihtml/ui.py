import base64
from enum import Enum
from typing import Union

import sublime

from .a import a
from .element import element


class OnClickType(Enum):
    URL = 1
    TEXT_COMMAND = 2
    WINDOW_COMMAND = 3
    APPLICATION_COMMAND = 4


class ImageType(Enum):
    PNG = 1
    JPEG = 2
    Base64 = 3


def _image_to_base64(type: ImageType, path: str) -> str:
    data = sublime.load_binary_resource(path)
    if type == ImageType.PNG:
        return f'data:image/png;base64,{base64.b64encode(data).decode("ascii")}'
    elif type == ImageType.JPEG:
        return f'data:image/jpeg;base64,{base64.b64encode(data).decode("ascii")}'
    elif type == ImageType.Base64:
        return path
    else:
        raise ValueError("Invalid image type")


class Card(element):
    def __init__(
        self,
        title: Union[str, element] = "",
        content: Union[str, element] = "",
        footer: Union[str, element] = "",
    ):
        super().__init__("div")
        self.bg_color("#fff").border("1px", "solid", "#ddd").set_style(
            "border-radius", ".25rem"
        ).m(".25rem")
        if isinstance(title, element):
            self.add_child(title)
        elif title:
            self.add_child(element("h3").add_content(title))

        if isinstance(content, element):
            self.add_child(content)
        elif content:
            self.add_child(element("div").add_content(content).p("1.25rem"))

        if isinstance(footer, element):
            self.add_child(footer)
        elif footer:
            self.add_child(element("div").add_content(footer))


class Button(element):
    def __init__(self, label: str, href: str = ""):
        super().__init__("a")

        self.bg_color("var(--background)")
        self.color("var(--foreground)")
        self.border_radius(".5rem")
        self.border("1px", "solid", "var(--foreground)")
        self.text_decoration_none()
        self.add_content(label)
        self.href(href)


class Checkbox(element):
    def __init__(
        self,
        label="",
        image_src="Packages/MiniHTML/minihtml/assets/checkbox-unchecked.png",
        is_checked=False,
    ):
        super().__init__("div")
        self.label = label
        self.is_checked = is_checked
        # Create the image element using the provided image source
        self.image = Image(src=image_src).width("2.5rem").height("2.5rem")
        # Create the anchor element wrapping the image
        self.anchor = a("#", "").set_attribute("checked", "false")
        # Add the checkbox input element
        # Combine all elements
        self.anchor.add_child(self.image)
        self.add_content(self.anchor.render() + self.label)

    def toggle(self):
        self.is_checked = not self.is_checked
        # Update the checkbox state visually if needed
        self.anchor.set_attribute("checked", "true" if self.is_checked else "false")


class Radio(element):
    def __init__(self, group_name, label="", is_selected=False):
        super().__init__("div")
        self.is_selected = is_selected
        self.group_name = group_name
        self.add_content(
            f"<label><input type='radio' name='{group_name}' {'checked' if is_selected else ''}> {label}</label>"
        )

    def select(self):
        self.is_selected = True
        # Update the radio button state visually if needed


class Link(element):
    def __init__(self, label: str, href: str = ""):
        super().__init__("a")

        self.bg_color("var(--background)")
        self.color("var(--foreground)")
        self.add_content(label)
        self.href(href)


class Icon(element):
    def __init__(self, src: str, image_type: ImageType = ImageType.PNG, alt: str = ""):
        super().__init__("img")

        try:
            image_src = _image_to_base64(image_type, src)
        except Exception:
            image_src = src

        self.set_attribute("src", image_src)
        self.set_attribute("alt", alt)
        self.bg_color("transparent")


class Image(element):
    def __init__(self, src: str, image_type: ImageType = ImageType.PNG, alt: str = ""):
        super().__init__("img")

        try:
            image_src = _image_to_base64(image_type, src)
        except Exception:
            image_src = src
        self.set_attribute("src", image_src)
        self.set_attribute("alt", alt)
