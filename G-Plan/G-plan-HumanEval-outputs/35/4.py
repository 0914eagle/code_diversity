
from typing import List

def make_a_pile(n: int) -> List[int]:
    stones = [n]
    for i in range(1, n):
        if i % 2 == 1:
            stones.append(n + 2 * i)
        else:
            stones.append(n + i)
    return stones

if __name__ == "__main__":
    n = int(input())
    result = make_a_pile(n)
    print(result)
