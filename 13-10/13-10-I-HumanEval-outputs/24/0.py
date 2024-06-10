
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    
    # Convert each number to binary string
    binary_strings = [format(num, "b") for num in arr]

    # Sort the array based on the number of ones in the binary representation
    sorted_arr = sorted(arr, key=lambda x: (binary_strings[x].count("1"), x))

    return sorted_arr

