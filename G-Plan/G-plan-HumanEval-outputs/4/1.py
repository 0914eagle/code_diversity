
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    def is_odd(num: int) -> bool:
        return num % 2 != 0

    first = array[0]
    last = array[-1]
    total = first + last

    if is_odd(total):
        return sorted(array)
    else:
        return sorted(array, reverse=True)

if __name__ == "__main__":
    array = list(map(int, input().strip().split()))
    result = sort_array(array)
    print(result)
