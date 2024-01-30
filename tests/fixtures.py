import pytest


@pytest.fixture
def input_dicts_for_splitting():
    return [
        {
            "dict1": {"key1": "value1"},
            "dict2": {"key2": "value2"}
        },
        {
            "dict1": {
                "key1": "value1",
                "key2": "value2"
            },
            "dict2": {
                "key3": "value3",
                "key4": {
                    "key5": "value5"
                }
            }
        }
    ]


@pytest.fixture
def expected_dicts_for_splitting():
    return [
        [
            {"key1": "value1"},
            {"key2": "value2"}
        ],
        [
            {
                "key1": "value1",
                "key2": "value2"
            },
            {
                "key3": "value3",
                "key4": {
                    "key5": "value5"
                }
            }
        ]
    ]


@pytest.fixture
def first_dict():
    return {
        "key1": "value1",
        "key2": {
            "key3": "value3"
        }
    }


@pytest.fixture
def second_dict():
    return {
        "key2": {
            "key4": "value4"
        },
        "key6": {
            "key8": "value8"
        }
    }


@pytest.fixture
def expected_result():
    return {
        "key1": "value1",
        "key2": {
            "key3": "value3",
            "key4": "value4"
        },
        "key6": {
            "key8": "value8"
        }
    }
