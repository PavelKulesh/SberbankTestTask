from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @classmethod
    @abstractmethod
    async def merge_trees(cls, trees: list[dict]) -> dict:
        pass

    @staticmethod
    @abstractmethod
    async def split_tree(tree: dict) -> list[dict]:
        pass
