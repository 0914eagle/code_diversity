
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Initialize a set to store the numbers in lst2
    numbers = set(lst2)
    # Loop through the elements of lst1 and add them to the appropriate set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    # Check if all the elements of lst1 are even
    if len(even_numbers) == len(lst1):
        return "YES"
    # Check if it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 even
    for num in odd_numbers:
        if num + 1 in numbers:
            even_numbers.add(num + 1)
            numbers.remove(num + 1)
        elif num - 1 in numbers:
            even_numbers.add(num - 1)
            numbers.remove(num - 1)
        else:
            return "NO"
    # Check if all the elements of lst1 are even after the exchange
    if len(even_numbers) == len(lst1):
        return "YES"
    else:
        return "NO"

