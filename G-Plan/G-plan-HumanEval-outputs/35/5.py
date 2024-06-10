
from typing import List

def make_a_pile(n: int) -> List[int]:
    def is_odd(num):
        return num % 2 != 0

    def calculate_stones(level, current_stones):
        if is_odd(level):
            return current_stones + 2
        else:
            return current_stones + 1

    stones = [n]
    for i in range(1, n):
        stones.append(calculate_stones(i, stones[-1]))

    return stones

if __name__ == "__main__":
    n = int(input().strip())
    result = make_a_pile(n)
    print(result)
