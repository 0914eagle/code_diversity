
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num):
        return num % 2 != 0

    first_element = array[0]
    last_element = array[-1]
    sum_first_last = first_element + last_element

    if is_odd(sum_first_last):
        return sorted(array)
    else:
        return sorted(array, reverse=True)

if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    result = sort_array(input_array)
    print(result)
