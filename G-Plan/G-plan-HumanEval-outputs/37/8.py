
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    return all(num < t for num in l)

# Test the function with the provided examples
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
