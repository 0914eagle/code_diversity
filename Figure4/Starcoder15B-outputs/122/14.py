def add_elements(arr, k):
    
    return sum(map(lambda x: x if x < 100 else 0, arr[:k]))
/tests/test_array_manipulation.py
import pytest

from src.array_manipulation import array_manipulation


@pytest.mark.parametrize(
    "n, queries, expected",
    [
        (5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]], 200),
        (10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]], 31),
    ],
)
