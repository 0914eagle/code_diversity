
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    
    # Convert each element in the array to its binary representation
    binary_repr = [bin(elem)[2:] for elem in arr]

    # Count the number of ones in each binary representation
    num_ones = [binary_repr[i].count('1') for i in range(len(binary_repr))]

    # Create a list of tuples, where each tuple contains the decimal value and the number of ones
    tuples = [(arr[i], num_ones[i]) for i in range(len(arr))]

    # Sort the list of tuples based on the number of ones and then the decimal value
    tuples.sort(key=lambda x: (x[1], x[0]))

    # Return the sorted array
    return [elem for elem, _ in tuples]

