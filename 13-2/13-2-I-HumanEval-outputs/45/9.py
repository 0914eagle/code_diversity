
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    
    result = ''
    for char in s:
        if char not in c:
            result += char
    return result, result == result[::-1]

