from typing import List


def string_xor(a: str, b: str) -> str:
    
    return ''.join(map(lambda x: '1' if x == '0' else '0', zip(a, b)))


