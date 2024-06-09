
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    total = sum(range(n, m+1))
    average = total // (m - n + 1)
    rounded_average = round(average)
    return f"0b{rounded_average:b}"

