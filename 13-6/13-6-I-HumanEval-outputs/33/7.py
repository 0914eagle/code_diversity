
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    average = (n + m) // 2
    rounded_average = round(average)
    return f"0b{rounded_average:b}"

