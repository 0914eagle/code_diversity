from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    max_len = 0
    max_str = None
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            max_str = s
    return max_str


if