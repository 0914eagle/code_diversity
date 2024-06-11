from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [value for value in values if isinstance(value, int)]
/tests/test_filter_integers.py
from filter_integers import filter_integers


