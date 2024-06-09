
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    # Convert a and b to the same type to make comparison easier
    if type(a) != type(b):
        if type(a) == int:
            a = float(a)
        elif type(a) == str:
            a = float(a.replace(',', '.'))
        if type(b) == int:
            b = float(b)
        elif type(b) == str:
            b = float(b.replace(',', '.'))
    
    # Compare a and b and return the larger one
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

