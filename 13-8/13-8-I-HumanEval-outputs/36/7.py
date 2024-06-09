
from typing import List

def add_elements(arr: List[int], k: int) -> int:
    
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the first k elements of the array
    for i in range(k):
        # Get the current element
        element = arr[i]
        # If the element has at most two digits, add it to the sum
        if len(str(element)) <= 2:
            sum += element
    # Return the sum
    return sum

