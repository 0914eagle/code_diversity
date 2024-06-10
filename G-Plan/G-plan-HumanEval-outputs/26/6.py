
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(input_list):
        freq_dict = {}
        for num in input_list:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        return freq_dict

    def find_greatest_integer_with_condition(freq_dict):
        max_val = -1
        for num, freq in freq_dict.items():
            if num > freq and freq > max_val:
                max_val = freq
        return max_val

    frequencies = count_frequency(lst)
    result = find_greatest_integer_with_condition(frequencies)
    return result

input_list = list(map(int, input().strip().split()))
print(search(input_list))
