
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(lst: List[int]) -> dict:
        freq_dict = {}
        for num in lst:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        return freq_dict

    def find_greatest_integer_with_condition(freq_dict: dict) -> int:
        result = -1
        for num, freq in freq_dict.items():
            if num > freq and freq >= result:
                result = freq
        return result

    freq_dict = count_frequency(lst)
    result = find_greatest_integer_with_condition(freq_dict)
    return result

# Input parsing and function call
input_list = list(map(int, input().strip().split()))
print(search(input_list))
