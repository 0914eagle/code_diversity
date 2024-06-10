
from typing import List

def add(lst: List[int]) -> int:
    def is_even(num: int) -> bool:
        return num % 2 == 0

    def at_odd_index(idx: int) -> bool:
        return idx % 2 != 0

    sum_even_odd_indices = sum(num for idx, num in enumerate(lst) if is_even(num) and at_odd_index(idx))
    return sum_even_odd_indices

if __name__ == "__main__":
    input_list = list(map(int, input().strip().split()))
    print(add(input_list))
