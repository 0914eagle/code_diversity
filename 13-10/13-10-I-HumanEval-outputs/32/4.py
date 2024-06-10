
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
    # If all the numbers in lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    # If not all the numbers in lst1 are even, try to find a pair of numbers to exchange
    for num1 in lst1:
        for num2 in lst2:
            # If the sum of the two numbers is even, exchange them and check if the resulting list is all even
            if num1 + num2 % 2 == 0:
                even_numbers.add(num1 + num2)
                even_numbers.discard(num1)
                even_numbers.discard(num2)
                if len(even_numbers) == len(lst1):
                    return "YES"
                # If the resulting list is not all even, revert the exchange and continue to the next pair of numbers
                even_numbers.add(num1)
                even_numbers.discard(num1 + num2)
    # If no pair of numbers can be exchanged to make all the elements of lst1 even, return "NO"
    return "NO"

