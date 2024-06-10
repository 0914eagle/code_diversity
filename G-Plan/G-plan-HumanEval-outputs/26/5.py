
from typing import List

def search(lst: List[int]) -> int:
    def count_frequencies(lst):
        freq_map = {}
        for num in lst:
            freq_map[num] = freq_map.get(num, 0) + 1
        return freq_map

    def find_greatest_integer_with_condition(freq_map):
        greatest_integer = -1
        for num, freq in freq_map.items():
            if num > freq and freq >= greatest_integer:
                greatest_integer = freq
        return greatest_integer if greatest_integer != -1 else -1

    frequencies = count_frequencies(lst)
    result = find_greatest_integer_with_condition(frequencies)
    return result

# Read input list
input_list = list(map(int, input().strip().split()))

# Call the search function and print the result
print(search(input_list))
