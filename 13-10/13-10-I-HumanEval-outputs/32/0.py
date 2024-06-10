
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the elements of lst1
    lst1_set = set(lst1)
    # Initialize a set to store the elements of lst2
    lst2_set = set(lst2)
    # Initialize a variable to store the result
    result = "YES"
    
    # Iterate through the elements of lst1
    for element in lst1:
        # If the element is odd, check if there is an even element in lst2 that can be exchanged
        if element % 2 == 1:
            # Check if there is an even element in lst2 that is not already in lst1
            for even_element in lst2_set:
                if even_element % 2 == 0 and even_element not in lst1_set:
                    # Exchange the elements and break the loop
                    lst1_set.add(even_element)
                    lst1_set.remove(element)
                    lst2_set.remove(even_element)
                    break
            # If no even element can be found, set the result to "NO"
            else:
                result = "NO"
                break
    
    # Return the result
    return result

