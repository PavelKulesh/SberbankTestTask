from src.abstract.service import AbstractService
from src.handlers.handler import Handler
from src.formatters.date_formatter import DateFormatter


class JSONService(AbstractService):
    @classmethod
    def parse(cls, tree: dict) -> dict:
        trees = Handler.split_tree(tree)
        merged_tree = Handler.merge_trees(trees=trees)
        DateFormatter.normalize(merged_tree)
        return merged_tree
