from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [int(x) for x in values if isinstance(x, int)]
