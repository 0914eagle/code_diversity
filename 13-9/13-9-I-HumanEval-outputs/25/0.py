
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the two intervals intersect
    if start1 <= end2 and start2 <= end1:
        # Get the start and end of the intersection
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)

        # Check if the length of the intersection is a prime number
        if is_prime(intersection_end - intersection_start + 1):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

