
from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if n > m:
        return -1

    avg = (n + m) // 2
    rounded_avg = round(avg)
    binary_avg = bin(rounded_avg)

    return binary_avg
