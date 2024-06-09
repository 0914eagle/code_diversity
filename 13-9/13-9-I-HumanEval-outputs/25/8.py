
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 <= start2:
        intersection_start = start2
    else:
        intersection_start = start1

    if end1 >= end2:
        intersection_end = end2
    else:
        intersection_end = end1

    if intersection_start <= intersection_end:
        length = intersection_end - intersection_start + 1
        if length == 1:
            return "NO"
        else:
            for i in range(2, int(length ** 0.5) + 1):
                if length % i == 0:
                    return "NO"
            return "YES"
    else:
        return "NO"

