
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # convert the list of integers to a list of strings
    x_str = [str(i) for i in x]
    # create a set to store the unique digits
    unique_digits_set = set()
    # iterate over the list of strings
    for num in x_str:
        # iterate over the digits of the number
        for digit in num:
            # if the digit is not even, add it to the set
            if digit not in "02468":
                unique_digits_set.add(digit)
    # convert the set back to a list and sort it
    unique_digits_list = sorted(list(unique_digits_set))
    # return the list of unique digits
    return unique_digits_list

