
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    
    total = sum(range(n, m+1))
    avg = total / (m - n + 1)
    rounded_avg = round(avg)
    binary_avg = bin(rounded_avg)[2:]
    return binary_avg

