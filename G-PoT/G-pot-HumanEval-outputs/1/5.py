
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None
    longest_str = max(strings, key=lambda x: (len(x), strings.index(x)))
    return longest_str
