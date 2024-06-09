
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    total = 0
    for i in range(n, m+1):
        total += i
    avg = total / (m - n + 1)
    rounded_avg = round(avg)
    return format(rounded_avg, 'b')

