
from typing import List

def add(lst: List[int]) -> int:
    def is_even(num: int) -> bool:
        return num % 2 == 0

    def at_odd_index(index: int) -> bool:
        return index % 2 == 1

    sum_even_odd_indices = sum(num for index, num in enumerate(lst) if is_even(num) and at_odd_index(index))
    return sum_even_odd_indices

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = add(input_list)
    print(result)
