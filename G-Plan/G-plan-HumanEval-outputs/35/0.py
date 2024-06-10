
from typing import List

def make_a_pile(n: int) -> List[int]:
    def is_odd(num: int) -> bool:
        return num % 2 != 0

    def calculate_stones(level: int, base_stones: int) -> int:
        if is_odd(level):
            return base_stones + 2 * (level // 2)
        else:
            return base_stones + level // 2

    if n == 0:
        return []

    pile = [n]
    for i in range(1, n):
        pile.append(calculate_stones(i, n))

    return pile

if __name__ == "__main__":
    n = int(input())
    result = make_a_pile(n)
    print(result)
