
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Initialize a variable to store the sum of the odd numbers in lst1
    odd_sum = 0
    
    # Iterate through lst1 and check if each number is even
    for num in lst1:
        if num % 2 == 0:
            # If the number is even, add it to the set of even numbers
            even_nums.add(num)
        else:
            # If the number is odd, add it to the sum of odd numbers
            odd_sum += num
    
    # Iterate through lst2 and check if each number is even
    for num in lst2:
        if num % 2 == 0:
            # If the number is even, add it to the set of even numbers
            even_nums.add(num)
        else:
            # If the number is odd, subtract it from the sum of odd numbers
            odd_sum -= num
    
    # If the sum of odd numbers is 0 and the set of even numbers is not empty, return "YES"
    if odd_sum == 0 and even_nums:
        return "YES"
    else:
        return "NO"

