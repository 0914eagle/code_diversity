
from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    
    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]
    
    largest_negative = max(negative_integers) if negative_integers else None
    smallest_positive = min(positive_integers) if positive_integers else None
    
    return largest_negative, smallest_positive
