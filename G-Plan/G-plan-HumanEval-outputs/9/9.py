
from typing import List

def add(lst: List[int]) -> int:
    def is_even(num: int) -> bool:
        return num % 2 == 0

    def at_odd_index(index: int) -> bool:
        return index % 2 != 0

    even_at_odd_indices = [num for index, num in enumerate(lst) if is_even(num) and at_odd_index(index)]
    return sum(even_at_odd_indices)

if __name__ == "__main__":
    lst = list(map(int, input().strip().split()))
    print(add(lst))
