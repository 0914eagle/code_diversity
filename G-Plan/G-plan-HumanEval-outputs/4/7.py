
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num):
        return num % 2 != 0

    def sum_first_last(arr):
        return arr[0] + arr[-1]

    sum_first_last_value = sum_first_last(array)
    sorted_array = sorted(array, reverse=is_odd(sum_first_last_value))

    return sorted_array.copy()

if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    result = sort_array(input_array)
    print(result)
