from abc import ABC, abstractmethod


class AbstractDateFormatter(ABC):
    @classmethod
    @abstractmethod
    def normalize(cls, tree: dict) -> None:
        pass
