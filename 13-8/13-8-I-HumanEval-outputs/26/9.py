
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    

    # Initialize a set to store the even numbers in lst1
    even_numbers = set()

    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)

    # If all the elements of lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"

    # Iterate through lst2 and check if any of the elements can be added to lst1 to make all the elements even
    for num in lst2:
        if num % 2 == 0 and num not in even_numbers:
            even_numbers.add(num)
            if len(even_numbers) == len(lst1):
                return "YES"

    # If no element can be added to make all the elements even, return "NO"
    return "NO"

