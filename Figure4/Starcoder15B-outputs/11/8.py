from typing import List


def string_xor(a: str, b: str) -> str:
    
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(a, b))


