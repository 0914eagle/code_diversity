
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num):
        return num % 2 != 0

    def sort_ascending(arr):
        return sorted(arr)

    def sort_descending(arr):
        return sorted(arr, reverse=True)

    first = array[0]
    last = array[-1]
    total = first + last

    if is_odd(total):
        return sort_ascending(array.copy())
    else:
        return sort_descending(array.copy())

if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    result = sort_array(input_array)
    print(result)
