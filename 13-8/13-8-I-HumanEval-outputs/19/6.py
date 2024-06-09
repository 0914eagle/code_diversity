
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if a == b:
        return None
    elif type(a) == int and type(b) == int:
        return max(a, b)
    elif type(a) == float and type(b) == float:
        return max(a, b)
    elif type(a) == str and type(b) == str:
        return max(a, b)
    elif type(a) == int and type(b) == float:
        return max(a, b)
    elif type(a) == float and type(b) == int:
        return max(a, b)
    elif type(a) == str and type(b) == int:
        return max(a, b)
    elif type(a) == int and type(b) == str:
        return max(a, b)
    elif type(a) == str and type(b) == float:
        return max(a, b)
    elif type(a) == float and type(b) == str:
        return max(a, b)
    else:
        raise ValueError("Invalid input types")

