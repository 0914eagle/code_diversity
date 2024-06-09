
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]
