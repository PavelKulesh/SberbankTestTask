from src.abstracts.handler import AbstractHandler


class Handler(AbstractHandler):
    @classmethod
    async def merge_trees(cls, trees: list[dict]) -> dict:
        merged_tree = {}
        for tree in trees:
            for key, value in tree.items():
                if key in merged_tree:
                    if isinstance(value, dict) and isinstance(merged_tree[key], dict):
                        merged_tree[key] = await cls.merge_trees([merged_tree[key], value])
                    else:
                        merged_tree[key] = [merged_tree[key], value]
                else:
                    merged_tree[key] = value
        return merged_tree

    @staticmethod
    async def split_tree(tree: dict) -> list[dict]:
        return [value for value in tree.values()]
