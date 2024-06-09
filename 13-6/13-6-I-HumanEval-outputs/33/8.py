
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    total = sum(range(n, m+1))
    avg = total / (m - n + 1)
    rounded = round(avg)
    return bin(rounded)[2:]

