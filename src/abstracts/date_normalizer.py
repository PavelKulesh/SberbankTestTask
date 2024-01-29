from abc import ABC, abstractmethod


class AbstractDateNormalizer(ABC):
    @classmethod
    @abstractmethod
    async def normalize(cls, tree: dict) -> None:
        pass
