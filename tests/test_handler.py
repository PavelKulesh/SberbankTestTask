from src.handlers.handler import Handler
from tests.fixtures import (input_dicts_for_splitting, expected_dicts_for_splitting,
                            first_dict, second_dict, expected_result)


def test_correct_splitting_dicts(input_dicts_for_splitting, expected_dicts_for_splitting):
    result = Handler.split_tree(input_dicts_for_splitting[0])
    assert result == expected_dicts_for_splitting[0]

    result = Handler.split_tree(input_dicts_for_splitting[1])
    assert result == expected_dicts_for_splitting[1]


def test_correct_merging_dicts(first_dict, second_dict, expected_result):
    result = Handler.merge_trees([first_dict, second_dict])
    assert result == expected_result
