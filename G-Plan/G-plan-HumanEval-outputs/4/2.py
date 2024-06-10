
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num):
        return num % 2 != 0

    def sort_in_ascending(arr):
        return sorted(arr)

    def sort_in_descending(arr):
        return sorted(arr, reverse=True)

    first_element = array[0]
    last_element = array[-1]
    sum_first_last = first_element + last_element

    if is_odd(sum_first_last):
        return sort_in_ascending(array)
    else:
        return sort_in_descending(array)

if __name__ == "__main__":
    input_array = list(map(int, input().strip().split()))
    result = sort_array(input_array)
    print(result)
