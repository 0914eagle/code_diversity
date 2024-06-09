
from typing import List

def add_elements(arr: List[int], k: int) -> int:
    
    # Initialize the sum to 0
    sum = 0
    # Iterate through the first k elements of the array
    for i in range(k):
        # If the element has at most two digits, add it to the sum
        if len(str(arr[i])) <= 2:
            sum += arr[i]
    # Return the sum
    return sum

