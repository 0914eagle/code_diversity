
from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return max(a, b)
        else:
            return a if a > float(b.replace(',', '.')) else None
    else:
        if isinstance(b, (int, float)):
            return b if float(a.replace(',', '.')) < b else None
        else:
            return a if float(a.replace(',', '.')) > float(b.replace(',', '.')) else None

