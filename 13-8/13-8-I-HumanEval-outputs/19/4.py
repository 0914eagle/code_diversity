
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if a == b:
        return None

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)

    if isinstance(a, str) and isinstance(b, str):
        return max(float(a.replace(',', '.')), float(b.replace(',', '.')))

    if isinstance(a, (int, float)) and isinstance(b, str):
        return max(a, float(b.replace(',', '.')))

    if isinstance(a, str) and isinstance(b, (int, float)):
        return max(float(a.replace(',', '.')), b)

    return None

