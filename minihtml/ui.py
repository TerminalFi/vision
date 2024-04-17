import base64
from enum import Enum
from typing import List

import sublime

from .tag import Tag


class ImageType(Enum):
    """
    An enumeration to represent different types of image formats supported.

    Attributes:
        PNG (int): Represents an image in Portable Network Graphics format.
        JPEG (int): Represents an image in Joint Photographic Experts Group format.
        Base64 (int): Indicates that the image is encoded in Base64 format, usually for embedding directly into web pages.
    """
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


class Spacer(Tag):
    """
    A class representing a spacer element implemented using an <img> tag without a source.
    This spacer is used to add horizontal space between elements in a layout.

    Attributes:
        space (int): The width of the spacer in rem units, with a default of 1 rem.

    Usage:
        The spacer uses an image tag with a specified width and no actual image displayed.
        It effectively serves as a horizontal gap or space in web layouts, using CSS to set its width.
    """

    def __init__(self, space: int = 1):
        super().__init__("img")
        self.space = space  # Define the amount of space (width) the spacer should take up

    def render(self):
        # Returns an HTML string for an image tag with the specified width and no image source
        return f'<img style="width: {self.space or 0}rem;">'


class Button(Tag):
    """
    A class representing a stylized button implemented as a hyperlink (<a> tag).
    This button is styled to look visually distinct and clickable, similar to traditional
    GUI buttons, but uses HTML hyperlink functionality for navigation.

    Attributes:
        label (str): The text displayed on the button.
        href (str): The URL to which the button links. If empty, the button will not link anywhere.

    Styling:
        The button uses background and foreground color variables for theming,
        includes a border, rounded corners for a modern look, and removes text decoration
        to avoid the underline commonly associated with hyperlinks.
    """

    def __init__(self, label: str, href: str = ""):
        super().__init__("a")
        self.bg_color("var(--background)")  # Set background color using a CSS variable
        self.color("var(--foreground)")  # Set text color using a CSS variable
        self.border_radius(".5rem")  # Rounded corners with a radius of .5 rem
        self.border("1px", "solid", "var(--foreground)")  # Solid border using the foreground color
        self.text_decoration_none()  # No underline or other text decoration
        self.content(label)  # Set the visible text on the button
        self.href(href)  # Set the hyperlink reference


class ButtonGroup:
    """
    A container for grouping multiple Button instances visually. This class applies
    uniform styling options to all buttons and specific border radius styles to the
    first and last buttons to visually separate them in the UI.

    Attributes:
        classes (List[str]): Optional CSS classes to apply to all buttons in the group.
        buttons (Button): Variable number of Button objects included in the group.

    The buttons are displayed in a row, with the outer buttons having squared corners
    on the outer edges to delineate the group boundaries.
    """
    def __init__(self, classes: List[str] = [], *buttons: Button):
        self.buttons = buttons
        self.classes = classes
        self.initialize_buttons()

    def initialize_buttons(self):
        for i, btn in enumerate(self.buttons):
            self.apply_edge_styles(btn, i)
            self.apply_classes()

    def apply_classes(self):
        for btn in self.buttons:
            for clazz in self.classes:
                btn.set_classes('append', clazz)

    def apply_edge_styles(self, btn, index):
        total = len(self.buttons)
        if index == 0:  # First button
            btn.border_top_right_radius('0pt').border_bottom_right_radius('0pt')
        elif index == total - 1:  # Last button
            btn.border_top_left_radius('0pt').border_bottom_left_radius('0pt')
        else:
            btn.border_radius('0pt')


class Link(Tag):
    """
    Represents a hyperlink (<a> tag) that is styled and clickable, used to navigate
    to specified URLs or to trigger actions within a web page.

    Attributes:
        label (str): The text displayed on the hyperlink.
        href (str): The URL the link points to. If empty, the hyperlink will not navigate anywhere.

    Styling:
        The link is styled with a background and foreground color defined by CSS variables.
        It serves both as navigational and aesthetic purposes in web interfaces.
    """
    def __init__(self, label: str, href: str = ""):
        super().__init__("a")
        self.bg_color("var(--background)")
        self.color("var(--foreground)")
        self.content(label)
        self.href(href)



class Icon(Tag):
    """
    Represents an image used as an icon on web pages, loaded from a specified source.
    The icon uses an <img> tag and can be of various types defined by the ImageType enum.

    Attributes:
        src (str): The path or URL to the icon image file.
        image_type (ImageType): The format of the image, defaults to PNG.
        alt (str): Alternative text for the image which describes the icon.

    Styling:
        The icon's background is set to transparent to blend seamlessly with the UI.
    """
    def __init__(self, src: str, image_type: ImageType = ImageType.PNG, alt: str = ""):
        super().__init__("img")
        try:
            image_src = _image_to_base64(image_type, src)
        except Exception:
            image_src = src
        self.set_attribute("src", image_src)
        self.set_attribute("alt", alt)
        self.bg_color("transparent")



class Image(Tag):
    """
    Represents a generic image element (<img>) on a web page, sourced from a given URL or path.
    It supports different image types, which are handled by converting to base64 format if necessary.

    Attributes:
        src (str): The source URL or path for the image file.
        image_type (ImageType): The format of the image, typically defaults to PNG.
        alt (str): Alternative text for the image, providing a textual description.

    Notes:
        The image attempts to convert the source file to base64 format for embedding directly in web pages,
        falling back to the original source if conversion fails.
    """
    def __init__(self, src: str, image_type: ImageType = ImageType.PNG, alt: str = ""):
        super().__init__("img")
        try:
            image_src = _image_to_base64(image_type, src)
        except Exception:
            image_src = src
        self.set_attribute("src", image_src)
        self.set_attribute("alt", alt)

