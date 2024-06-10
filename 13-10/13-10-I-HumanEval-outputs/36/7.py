
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # your code here
    result = []
    for num in x:
        if all(str(num)[i] % 2 != 0 for i in range(len(str(num)))):
            result.append(num)
    return sorted(result)

