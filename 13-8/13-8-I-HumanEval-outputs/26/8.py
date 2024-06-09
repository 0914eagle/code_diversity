
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    

    # Initialize a set to store the even numbers in lst1
    even_nums = set()

    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)

    # If all the elements of lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"

    # If not all the elements of lst1 are even, try to find a way to exchange elements
    # between lst1 and lst2 to make all the elements of lst1 even
    for num in lst1:
        if num % 2 == 1:
            # Find the corresponding even number in lst2 that is closest to num
            closest_even = find_closest_even(num, lst2)

            # If there is no even number in lst2 that is closer to num, return "NO"
            if closest_even is None:
                return "NO"

            # Remove the even number from lst2 and add it to lst1
            lst2.remove(closest_even)
            lst1.append(closest_even)

    # If all the elements of lst1 are even after the exchange, return "YES"
    return "YES"

def find_closest_even(num: int, lst: List[int]) -> int:
    

    # Initialize the minimum difference to infinity
    min_diff = float("inf")

    # Initialize the closest even number to None
    closest_even = None

    # Iterate through lst and find the closest even number to num
    for even_num in lst:
        if even_num % 2 == 0:
            diff = abs(even_num - num)
            if diff < min_diff:
                min_diff = diff
                closest_even = even_num

    return closest_even

