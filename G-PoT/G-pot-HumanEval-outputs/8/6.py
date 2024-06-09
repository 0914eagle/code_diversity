
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []

    max_values = []
    current_max = float('-inf')
    
    for num in numbers:
        current_max = max(current_max, num)
        max_values.append(current_max)
    
    return max_values
