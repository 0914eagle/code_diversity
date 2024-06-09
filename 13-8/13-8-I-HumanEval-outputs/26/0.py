
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
    # Initialize a boolean to keep track of whether it is possible to make lst1 all even
    possible = True
    # Iterate through lst2 and check if any of the numbers can be added to even_numbers to make it all even
    for num in lst2:
        if num % 2 == 0 and num not in even_numbers:
            even_numbers.add(num)
        elif num % 2 == 1 and num not in even_numbers:
            possible = False
            break
    # Return "YES" if it is possible to make lst1 all even, otherwise return "NO"
    if possible:
        return "YES"
    else:
        return "NO"

