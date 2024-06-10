
from typing import List

def search(lst: List[int]) -> int:
    def count_frequencies(lst: List[int]) -> dict:
        freq_dict = {}
        for num in lst:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        return freq_dict

    def find_greatest_integer(freq_dict: dict) -> int:
        greatest_integer = -1
        for num, freq in freq_dict.items():
            if num > greatest_integer and freq >= num:
                greatest_integer = num
        return greatest_integer

    frequencies = count_frequencies(lst)
    result = find_greatest_integer(frequencies)
    return result

# Read input list from user
input_list = list(map(int, input().split()))

# Call the search function and print the result
print(search(input_list))
