
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    
    start1, end1 = interval1
    start2, end2 = interval2

    if start1 <= start2:
        if end1 < start2 or end2 < start1:
            return "NO"
        else:
            length = min(end1, end2) - max(start1, start2) + 1
    else:
        if end2 < start1 or end1 < start2:
            return "NO"
        else:
            length = min(end2, end1) - max(start2, start1) + 1

    if length == 1:
        return "NO"
    else:
        for i in range(2, int(length ** 0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES"

