import threading
from typing import Any


class Context:
    def __init__(self):
        self.current: Any = None
        self._lock = threading.RLock()

    def push(self, instance):
        with self._lock:
            if self.current is None:
                instance.parent = None
            else:
                instance.parent = self.current
            self.current = instance  # Set current context to the new instance

    def pop(self, instance):
        with self._lock:
            self.current = instance.parent
