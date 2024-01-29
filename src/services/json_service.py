from src.abstracts.service import AbstractService
from src.handlers.handler import Handler
from src.normalizers.date_normalizer import DateNormalizer


class JSONService(AbstractService):
    @classmethod
    async def parse(cls, tree: dict) -> dict:
        trees = await Handler.split_tree(tree)
        parsed_tree = await Handler.merge_trees(trees=trees)
        await DateNormalizer.normalize(parsed_tree)
        return parsed_tree
