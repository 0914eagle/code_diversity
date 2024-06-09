
from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    
    negative_integers = []
    positive_integers = []

    for num in lst:
        if num < 0:
            negative_integers.append(num)
        elif num > 0:
            positive_integers.append(num)

    largest_negative_integer = None
    smallest_positive_integer = None

    if negative_integers:
        largest_negative_integer = max(negative_integers)

    if positive_integers:
        smallest_positive_integer = min(positive_integers)

    return (largest_negative_integer, smallest_positive_integer)

