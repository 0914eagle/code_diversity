from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    # TODO: Implement this function
    pass
/tests/test_find_closest_elements.py
from typing import List, Tuple

import pytest

from exercises.find_closest_elements import find_closest_elements


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.1], (2.0, 2.1)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.3], (2.0, 2.3)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.4], (2.0, 2.4)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.5], (2.0, 2.5)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.6], (2.0, 2.6)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.7], (2.0, 2.7)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.8], (2.0, 2.8)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.9], (2.0, 2.9)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 3.0], (2.0