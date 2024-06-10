
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num: int) -> bool:
        return num % 2 != 0

    def sort_asc(array: List[int]) -> List[int]:
        return sorted(array)

    def sort_desc(array: List[int]) -> List[int]:
        return sorted(array, reverse=True)

    first = array[0]
    last = array[-1]
    sum_first_last = first + last

    if is_odd(sum_first_last):
        return sort_asc(array)
    else:
        return sort_desc(array)

if __name__ == "__main__":
    input_array = list(map(int, input().strip().split()))
    result = sort_array(input_array)
    print(result)
