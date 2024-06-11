from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    strings.sort(key=lambda s: len(s), reverse=True)
    return strings[0]


if