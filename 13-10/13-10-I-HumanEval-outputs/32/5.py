
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set(num for num in lst1 if num % 2 == 0)
    # Initialize a set to store the odd numbers in lst1
    odd_nums = set(num for num in lst1 if num % 2 == 1)
    # Initialize a set to store the elements in lst2
    lst2_set = set(lst2)
    # Iterate through the odd numbers in lst1 and check if there is a corresponding even number in lst2
    for odd_num in odd_nums:
        if odd_num + 1 in lst2_set:
            # If there is a corresponding even number, add it to the set of even numbers and remove both numbers from the lst1 and lst2 sets
            even_nums.add(odd_num + 1)
            lst1_set.remove(odd_num)
            lst1_set.remove(odd_num + 1)
            lst2_set.remove(odd_num)
            lst2_set.remove(odd_num + 1)
    # If all the elements in lst1 are even, return "YES"
    if not lst1_set:
        return "YES"
    # Otherwise, return "NO"
    return "NO"

