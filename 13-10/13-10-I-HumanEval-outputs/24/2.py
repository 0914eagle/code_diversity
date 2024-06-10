
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    
    # Convert each integer to binary string
    bin_strs = [bin(x)[2:] for x in arr]
    # Get the number of ones in each binary string
    num_ones = [s.count("1") for s in bin_strs]
    # Sort the numbers based on the number of ones and then the decimal value
    sorted_arr = sorted(arr, key=lambda x: (num_ones[arr.index(x)], x))
    return sorted_arr

