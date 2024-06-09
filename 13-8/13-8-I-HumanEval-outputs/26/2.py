
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to keep track of the elements in lst1
    elements = set(lst1)
    # Initialize a flag to keep track of whether all elements in lst1 are even
    all_even = True
    # Iterate through the elements in lst2
    for element in lst2:
        # If the current element is even and not already in lst1, add it to the set
        if element % 2 == 0 and element not in elements:
            elements.add(element)
        # If the current element is odd and already in lst1, set the flag to False
        elif element % 2 == 1 and element in elements:
            all_even = False
    # If all elements in lst1 are even, return "YES", otherwise return "NO"
    return "YES" if all_even else "NO"

