
from typing import List

def search(lst: List[int]) -> int:
    def count_frequency(lst: List[int]) -> dict:
        freq_map = {}
        for num in lst:
            freq_map[num] = freq_map.get(num, 0) + 1
        return freq_map

    def find_greatest_integer_with_condition(freq_map: dict) -> int:
        result = -1
        for num, freq in freq_map.items():
            if num > 0 and freq >= num:
                result = max(result, num)
        return result

    frequency_map = count_frequency(lst)
    result = find_greatest_integer_with_condition(frequency_map)
    return result

# Read input
input_list = list(map(int, input().split()))

# Call the search function and print the result
print(search(input_list))
