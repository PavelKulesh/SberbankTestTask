from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @classmethod
    @abstractmethod
    def merge_trees(cls, trees: list[dict]) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def split_tree(tree: dict) -> list[dict]:
        raise NotImplementedError
