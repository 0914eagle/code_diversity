
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 <= end2 and start2 <= end1:
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)
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

