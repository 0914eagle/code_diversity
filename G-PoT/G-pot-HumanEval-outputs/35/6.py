
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if n > m:
        return -1
    avg = (n + m) // 2
    binary_avg = bin(round(avg))
    return binary_avg
