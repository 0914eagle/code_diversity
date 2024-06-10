
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(input_list):
        freq_dict = {}
        for num in input_list:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        return freq_dict

    freq_map = count_frequency(lst)
    result = -1
    for num, freq in freq_map.items():
        if freq >= num and num > result:
            result = num
    return result

# Test cases
print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
