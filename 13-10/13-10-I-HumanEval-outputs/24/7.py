
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    
    # convert each element to its binary representation
    binary_repr = [format(x, 'b') for x in arr]

    # count the number of ones in each element's binary representation
    num_ones = [bin_rep.count('1') for bin_rep in binary_repr]

    # sort the elements based on the number of ones in their binary representation, and then by their decimal value
    sorted_indices = sorted(range(len(arr)), key=lambda i: (num_ones[i], arr[i]))

    return [arr[i] for i in sorted_indices]

