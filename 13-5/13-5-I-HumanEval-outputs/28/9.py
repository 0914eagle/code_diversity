
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Initialize a set to store the numbers in lst2
    numbers = set(lst2)
    
    # Iterate through lst1 and add even and odd numbers to their respective sets
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    
    # If all the numbers in lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    
    # If there are no odd numbers in lst1, return "NO"
    if not odd_numbers:
        return "NO"
    
    # Iterate through the odd numbers in lst1 and check if they have a corresponding even number in lst2
    for odd_num in odd_numbers:
        even_num = odd_num + 1
        if even_num in numbers:
            even_numbers.add(even_num)
            numbers.remove(even_num)
    
    # If all the numbers in lst1 are even after the exchange, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    
    # Otherwise, return "NO"
    return "NO"

