
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    
    # Convert each number to binary and count the number of ones
    binary_counts = [(bin(num)[2:].count("1"), num) for num in arr]
    # Sort the array based on the number of ones and then on the decimal value
    return [num for (_, num) in sorted(binary_counts)]

