import threading
from typing import Any, Optional

from .a import a
from .b import b
from .big import big
from .body import body
from .br import br
from .code import code
from .div import div
from .em import em
from .h1 import h1
from .h2 import h2
from .h3 import h3
from .h4 import h4
from .h5 import h5
from .h6 import h6
from .head import head
from .hr import hr
from .html import html
from .i import i
from .img import img
from .li import li
from .ol import ol
from .p import p
from .renderable import BaseTag
from .small import small
from .span import span
from .strong import strong
from .style import style
from .tag import tag
from .text import Text as text
from .tt import tt
from .types import ContextBase
from .u import u
from .ul import ul
from .var import var


class Context(ContextBase):
    def __init__(self):
        self.current: Any = None
        self._lock = threading.RLock()

    def push(self, instance):
        with self._lock:
            if self.current is None:
                instance.parent = None
            else:
                instance.parent = self.current
            self.current = instance

    def pop(self, instance):
        with self._lock:
            self.current = instance.parent

    def a(self, href: Optional[str], content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return a(self, href, content, *args, **kwargs)

    def b(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return b(self, content, *args, **kwargs)

    def big(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return big(self, content, *args, **kwargs)

    def body(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return body(self, content, *args, **kwargs)

    def br(self, *args, **kwargs) -> BaseTag:
        return br(self, *args, **kwargs)

    def code(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return code(self, content, *args, **kwargs)

    def div(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return div(self, content, *args, **kwargs)

    def em(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return em(self, content, *args, **kwargs)

    def h1(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h1(self, content, *args, **kwargs)

    def h2(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h2(self, content, *args, **kwargs)

    def h3(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h3(self, content, *args, **kwargs)

    def h4(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h4(self, content, *args, **kwargs)

    def h5(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h5(self, content, *args, **kwargs)

    def h6(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return h6(self, content, *args, **kwargs)

    def head(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return head(self, content, *args, **kwargs)

    def hr(self, *args, **kwargs) -> BaseTag:
        return hr(self, *args, **kwargs)

    def html(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return html(self, content, *args, **kwargs)

    def i(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return i(self, content, *args, **kwargs)

    def img(self, src: Optional[str], *args, **kwargs) -> BaseTag:
        return img(self, src, *args, **kwargs)

    def li(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return li(self, content, *args, **kwargs)

    def ol(self, *args, **kwargs) -> BaseTag:
        return ol(self, *args, **kwargs)

    def p(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return p(self, content, *args, **kwargs)

    def small(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return small(self, content, *args, **kwargs)

    def span(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return span(self, content, *args, **kwargs)

    def strong(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return strong(self, content, *args, **kwargs)

    def style(self, default_css: dict, *args, **kwargs) -> BaseTag:
        return style(self, default_css, *args, **kwargs)

    def tag(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return tag(self, content, *args, **kwargs)

    def text(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return text(self, content, *args, **kwargs)

    def tt(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return tt(self, content, *args, **kwargs)

    def u(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return u(self, content, *args, **kwargs)

    def ul(self, *args, **kwargs) -> BaseTag:
        return ul(self, *args, **kwargs)

    def var(self, content: Optional[str] = None, *args, **kwargs) -> BaseTag:
        return var(self, content, *args, **kwargs)
