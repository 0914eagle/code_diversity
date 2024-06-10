
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(lst):
        freq_map = {}
        for num in lst:
            freq_map[num] = freq_map.get(num, 0) + 1
        return freq_map

    def find_greatest_integer_with_condition(freq_map):
        max_val = -1
        for num, freq in freq_map.items():
            if num > freq and freq > max_val:
                max_val = freq
        return max_val

    freq_map = count_frequency(lst)
    result = find_greatest_integer_with_condition(freq_map)
    return result

# Test cases
print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
