from abc import ABC, abstractmethod


class AbstractService(ABC):
    @classmethod
    @abstractmethod
    async def parse(cls, tree: str | dict) -> dict:
        pass
