import pytest

from src.handlers.handler import Handler
from tests.data_for_tests import (input_dicts_for_splitting, expected_dicts_for_splitting,
                                  first_dict, second_dict, expected_result)


@pytest.mark.parametrize("input_dict, expected_output", (
        (input_dicts_for_splitting[0], expected_dicts_for_splitting[0]),
        (input_dicts_for_splitting[1], expected_dicts_for_splitting[1])
))
def test_correct_splitting_dicts(input_dict, expected_output):
    result = Handler.split_tree(input_dict)
    assert result == expected_output


@pytest.mark.parametrize("first_input_dict, second_input_dict, expected_output", (
        (first_dict, second_dict, expected_result),
))
def test_correct_merging_dicts(first_input_dict, second_input_dict, expected_output):
    result = Handler.merge_trees([first_input_dict, second_input_dict])
    assert result == expected_output
