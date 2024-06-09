
from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    
    result = ''.join([char for char in s if char not in c])
    return result, result == result[::-1]

