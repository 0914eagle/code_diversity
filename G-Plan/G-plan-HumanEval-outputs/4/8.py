
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def get_sum_first_last(arr: List[int]) -> int:
        return arr[0] + arr[-1]

    def sort_ascending(arr: List[int]) -> List[int]:
        return sorted(arr)

    def sort_descending(arr: List[int]) -> List[int]:
        return sorted(arr, reverse=True)

    sum_first_last = get_sum_first_last(array)
    if sum_first_last % 2 == 0:
        return sort_descending(array)
    else:
        return sort_ascending(array)

if __name__ == "__main__":
    input_array = list(map(int, input().strip().split()))
    result = sort_array(input_array)
    print(result)
