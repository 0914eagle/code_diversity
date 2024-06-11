from typing import List


def string_xor(a: str, b: str) -> str:
    
    return "".join(["1" if int(a_i) ^ int(b_i) else "0" for a_i, b_i in zip(a, b)])


