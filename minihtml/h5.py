from typing import Optional

from .tag import Tag


class h5(Tag):
    """
    Represents the 'h5' HTML tag, used for headings at the fifth level in HTML documents. This tag is generally
    employed for sub-sub-section headings within the structure defined by higher-level headings (h1-h4), providing
    detailed organizational layers and helping to present information in a clearly segmented manner.

    Example usage:
        h5(content="Further Insights into Sub-Topic")
    """

    def __init__(self, content: Optional[str] = None, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)
        if content:
            self.content(content)
