
from typing import List

def calculate_stones(n: int, level: int) -> int:
    if level % 2 == 1:
        return n + 2 * (level // 2)
    else:
        return n + (level // 2)

def make_a_pile(n: int) -> List[int]:
    if n == 0:
        return []
    
    levels = [calculate_stones(n, i) for i in range(1, n + 1)]
    return levels

if __name__ == "__main__":
    n = int(input())
    result = make_a_pile(n)
    print(result)
