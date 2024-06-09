
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Initialize a set to store the odd numbers in lst1
    odd_nums = set()
    # Initialize a set to store the numbers in lst2
    nums = set(lst2)

    # Iterate through lst1 and check if each number is even or odd
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
        else:
            odd_nums.add(num)

    # If all numbers in lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"

    # If there are no odd numbers in lst1, return "NO"
    if not odd_nums:
        return "NO"

    # If there are odd numbers in lst1, check if there are corresponding even numbers in lst2
    for num in odd_nums:
        if num + 1 in nums:
            even_nums.add(num + 1)
            odd_nums.remove(num)
            nums.remove(num + 1)

    # If all odd numbers in lst1 have corresponding even numbers in lst2, return "YES"
    if not odd_nums:
        return "YES"

    # If there are still odd numbers left in lst1 and no corresponding even numbers in lst2, return "NO"
    return "NO"

