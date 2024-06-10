
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(lst):
        freq_map = {}
        for num in lst:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        return freq_map

    freq_map = count_frequency(lst)
    result = -1
    for num, freq in freq_map.items():
        if num > 0 and freq >= num:
            if result == -1 or num > result:
                result = num
    return result

# Test the function with the provided examples
print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
