from abc import ABC, abstractmethod


class renderable(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
