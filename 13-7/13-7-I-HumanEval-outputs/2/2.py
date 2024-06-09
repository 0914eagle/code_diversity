
from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    
    negative_integers = []
    positive_integers = []

    for num in lst:
        if num < 0:
            negative_integers.append(num)
        elif num > 0:
            positive_integers.append(num)

    largest_negative = None if not negative_integers else max(negative_integers)
    smallest_positive = None if not positive_integers else min(positive_integers)

    return largest_negative, smallest_positive

