
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if a == b:
        return None

    a_type = type(a)
    b_type = type(b)

    if a_type == b_type:
        return max(a, b)
    elif a_type == int and b_type == float:
        return b
    elif a_type == float and b_type == int:
        return a
    elif a_type == str and b_type == int:
        return b
    elif a_type == int and b_type == str:
        return a
    elif a_type == str and b_type == float:
        return b
    elif a_type == float and b_type == str:
        return a
    else:
        return None

