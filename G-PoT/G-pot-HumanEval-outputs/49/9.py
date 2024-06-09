
from typing import Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    start1, end1 = interval1
    start2, end2 = interval2
    
    if end1 < start2 or end2 < start1:
        return 'NO'
    
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    intersection_length = intersection_end - intersection_start + 1
    
    if intersection_length <= 0:
        return 'NO'
    
    if is_prime(intersection_length):
        return 'YES'
    else:
        return 'NO'

# Test cases
print(intersection((1, 2), (2, 3)))  # 'NO'
print(intersection((-1, 1), (0, 4)))  # 'NO'
print(intersection((-3, -1), (-5, 5)))  # 'YES'
