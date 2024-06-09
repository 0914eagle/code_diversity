
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if a == b:
        return None
    elif a > b:
        return a
    elif b > a:
        return b

