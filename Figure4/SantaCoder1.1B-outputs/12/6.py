from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    if len(strings) == 1:
        return strings[0]

    return max(strings, key=len)
