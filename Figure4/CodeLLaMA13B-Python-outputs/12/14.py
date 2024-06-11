from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    max_string = strings[0]
    for string in strings:
        if len(string) > len(max_string):
            max_string = string
    return max_string


if