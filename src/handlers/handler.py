from src.abstract.handler import AbstractHandler


class Handler(AbstractHandler):
    @classmethod
    def merge_trees(cls, trees: list[dict]) -> dict:
        """
        Method that takes a list of dictionaries and merges
        them into the resulting dictionary (tree).
        If a value is a dictionary and the key already exists
        in the resulting dictionary, recursive updating of this dictionary occurs.
        """
        merged_tree = {}
        for tree in trees:
            for key, value in tree.items():
                if key in merged_tree:
                    if isinstance(value, dict) and isinstance(merged_tree[key], dict):
                        merged_tree[key] = cls.merge_trees([merged_tree[key], value])
                    else:
                        merged_tree[key] = [merged_tree[key], value] if not isinstance(merged_tree[key], list) else \
                            merged_tree[key] + [value]
                else:
                    merged_tree[key] = value
        return merged_tree

    @staticmethod
    def split_tree(tree: dict) -> list[dict]:
        """
        The method takes a dictionary containing multiple trees,
        separates them, and returns a list of these trees.
        """
        return [sub_tree for sub_tree in tree.values()]
