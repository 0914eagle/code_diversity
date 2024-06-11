from typing import List


def string_xor(a: str, b: str) -> str:
    
    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))


