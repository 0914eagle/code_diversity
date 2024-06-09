
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if a == b:
        return None

    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)

    if isinstance(a, float) and isinstance(b, float):
        return max(a, b)

    if isinstance(a, str) and isinstance(b, str):
        a_float = float(a.replace(',', '.'))
        b_float = float(b.replace(',', '.'))
        return str(max(a_float, b_float))

    raise TypeError("a and b must be of the same type")

