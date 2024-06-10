
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    
    # Check if the array is empty
    if not arr:
        return True
    
    # Initialize a variable to keep track of the minimum element
    min_element = arr[0]
    
    # Iterate over the array and check if the element is greater than or equal to the minimum element
    for element in arr:
        if element < min_element:
            return False
        min_element = element
    
    # If all the elements are in non-decreasing order, return True
    return True

