
from typing import Tuple

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    start1, end1 = interval1
    start2, end2 = interval2
    
    if end1 < start2 or end2 < start1:
        return 'NO'
    
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    intersection_length = intersection_end - intersection_start + 1
    
    if is_prime(intersection_length):
        return 'YES'
    else:
        return 'NO'
