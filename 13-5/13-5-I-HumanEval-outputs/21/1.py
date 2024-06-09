
from typing import List

def solution(lst: List[int]) -> int:
    
    # Initialize an empty list to store the odd elements in even positions
    odd_even_sum = 0
    
    # Iterate through the list and check if the element is odd and in an even position
    for i, element in enumerate(lst):
        if element % 2 != 0 and i % 2 == 0:
            odd_even_sum += element
    
    # Return the sum of the odd elements in even positions
    return odd_even_sum

