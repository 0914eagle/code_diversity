
from typing import List


def string_xor(a: str, b: str) -> str:
    
    result = ''
    for i, j in zip(a, b):
        if i == j:
            result += '0'
        else:
            result += '1'
    return result

