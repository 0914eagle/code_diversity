from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    longest_string = max(strings, key=len)
    for string in strings:
        if len(string) == len(longest_string):
            return string
    return longest_string


if