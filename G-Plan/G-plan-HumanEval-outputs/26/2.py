
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(input_list):
        freq_dict = {}
        for num in input_list:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        return freq_dict

    def find_greatest_integer_with_condition(freq_dict):
        greatest_integer = -1
        for num, freq in freq_dict.items():
            if num > freq and freq >= greatest_integer:
                greatest_integer = freq
        return greatest_integer

    freq_dict = count_frequency(lst)
    result = find_greatest_integer_with_condition(freq_dict)
    return result

# Test cases
print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
