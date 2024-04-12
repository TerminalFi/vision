from abc import ABC, abstractmethod


class Renderable(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
