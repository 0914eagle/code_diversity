
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(lst):
        freq = {}
        for num in lst:
            freq[num] = freq.get(num, 0) + 1
        return freq

    def find_greatest_integer(freq):
        greatest_integer = -1
        for num, count in freq.items():
            if num > greatest_integer and count >= num:
                greatest_integer = num
        return greatest_integer

    frequency_map = count_frequency(lst)
    result = find_greatest_integer(frequency_map)
    return result

# Test the function with example inputs
print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
