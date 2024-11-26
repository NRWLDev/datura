import pytest

import datura


@pytest.mark.parametrize(
    ("input_dict", "expected"),
    [
        ({"a": "b"}, {"a": "b"}),
        ({"a": {"b": "c"}}, {"a.b": "c"}),
        (
            {
                "a": 1,
                "b": {
                    "c": 2,
                    "d": {
                        "e": 3,
                        "f": 4,
                    },
                },
                "g": {
                    "h": 5,
                },
            },
            {
                "a": 1,
                "b.c": 2,
                "b.d.e": 3,
                "b.d.f": 4,
                "g.h": 5,
            },
        ),
        (
            {
                "a": "string",
                "b": {
                    "c": True,
                    "d": {
                        "e": False,
                        "f": ["a", "list"],
                    },
                },
                "g": {
                    "h": {"a", "set"},
                },
            },
            {
                "a": "string",
                "b.c": True,
                "b.d.e": False,
                "b.d.f": ["a", "list"],
                "g.h": {"a", "set"},
            },
        ),
    ],
)
def test_flatten_dict(input_dict, expected):
    assert datura.flatten_dict(input_dict) == expected


@pytest.mark.parametrize(
    "input_",
    [
        "string",
        True,
        1,
        ["a", "list"],
        {"a", "set"},
    ],
)
def test_handle_invalid_input(input_):
    datura.flatten_dict(input_)
