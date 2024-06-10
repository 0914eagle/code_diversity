
from typing import List

def make_a_pile(n: int) -> List[int]:
    def calculate_stones(level: int, is_odd: bool) -> int:
        if is_odd:
            return n + 2 * level - 1
        else:
            return n + level

    if n == 0:
        return []

    pile = [n]
    for i in range(1, n):
        is_odd = i % 2 == 1
        stones = calculate_stones(i, is_odd)
        pile.append(stones)

    return pile

if __name__ == "__main__":
    n = int(input().strip())
    result = make_a_pile(n)
    print(result)
