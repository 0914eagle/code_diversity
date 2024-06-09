
from typing import List

def sort_array(arr: List[int]) -> List[int]:
    def count_ones(num):
        return bin(num).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))
