
from typing import List

def sort_even(l: List[int]) -> List[int]:
    
    # Initialize an empty list to store the sorted even values
    sorted_even = []
    # Iterate through the input list and append the even values to the sorted_even list
    for i in range(0, len(l), 2):
        sorted_even.append(l[i])
    # Sort the sorted_even list
    sorted_even.sort()
    # Initialize an empty list to store the output list
    output = []
    # Iterate through the input list and append the values to the output list
    for i in range(len(l)):
        if i % 2 == 0:
            output.append(sorted_even[i // 2])
        else:
            output.append(l[i])
    return output

