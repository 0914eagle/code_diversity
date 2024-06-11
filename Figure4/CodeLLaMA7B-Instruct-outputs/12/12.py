
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    longest_string = None
    for string in strings:
        if longest_string is None or len(string) > len(longest_string):
            longest_string = string

    return longest_string

