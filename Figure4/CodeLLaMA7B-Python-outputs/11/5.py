from typing import List


def string_xor(a: str, b: str) -> str:
    
    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


