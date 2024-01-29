from abc import ABC, abstractmethod


class AbstractDateNormalizer(ABC):
    @classmethod
    @abstractmethod
    def normalize(cls, tree: dict) -> None:
        pass
