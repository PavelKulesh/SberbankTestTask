from src.abstract.handler import AbstractHandler


class Handler(AbstractHandler):
    @classmethod
    def merge_trees(cls, trees: list[dict]) -> dict:
        """
        Метод, который принимает список словарей и объединяет их в результирующий словарь (дерево).
        Если значение является словарем и ключ уже существует в результирующем словаре,
        то происходит рекурсивное обновление этого словаря.

        :param trees: список деревьев
        :return: объединенный словарь (дерево)
        """
        merged_tree = {}
        for tree in trees:
            for key, value in tree.items():
                if key in merged_tree:
                    if isinstance(value, dict) and isinstance(merged_tree[key], dict):
                        merged_tree[key] = cls.merge_trees([merged_tree[key], value])
                    else:
                        merged_tree[key] = [merged_tree[key], value]
                else:
                    merged_tree[key] = value
        return merged_tree

    @staticmethod
    def split_tree(tree: dict) -> list[dict]:
        """
        Метод принимает словарь, содержащий несколько деревьев,
        разделяет их и возвращает список этих деревьев.
        """
        return [sub_tree for sub_tree in tree.values()]
