
from typing import List

def sort_array(array: List[int]) -> List[int]:
    def is_odd(num: int) -> bool:
        return num % 2 != 0

    def sort_ascending(arr: List[int]) -> List[int]:
        return sorted(arr)

    def sort_descending(arr: List[int]) -> List[int]:
        return sorted(arr, reverse=True)

    if not array:
        return []

    first = array[0]
    last = array[-1]
    total_sum = first + last

    if is_odd(total_sum):
        return sort_ascending(array.copy())
    else:
        return sort_descending(array.copy())

if __name__ == "__main__":
    input_array = list(map(int, input().strip().split(',')))
    result = sort_array(input_array)
    print(result)
