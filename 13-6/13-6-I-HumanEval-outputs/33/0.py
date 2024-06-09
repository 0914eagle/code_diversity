
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    
    if n > m:
        return -1
    
    sum = 0
    for i in range(n, m+1):
        sum += i
    
    avg = sum / (m - n + 1)
    rounded_avg = round(avg)
    return format(rounded_avg, 'b')

