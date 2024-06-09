
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    # Convert all values to float
    a_float = float(a.replace(",", "."))
    b_float = float(b.replace(",", "."))

    # Compare values and return larger one
    if a_float > b_float:
        return a
    elif a_float < b_float:
        return b
    else:
        return None

