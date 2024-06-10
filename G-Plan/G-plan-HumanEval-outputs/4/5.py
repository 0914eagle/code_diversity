
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num):
        return num % 2 != 0

    def sort_odd(array):
        return sorted(array)

    def sort_even(array):
        return sorted(array, reverse=True)

    first = array[0]
    last = array[-1]
    total_sum = first + last

    if is_odd(total_sum):
        return sort_odd(array)
    else:
        return sort_even(array)

if __name__ == "__main__":
    input_array = list(map(int, input().strip().split()))
    result = sort_array(input_array)
    print(result)
