
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    return all(num < t for num in l)

l = list(map(int, input().split()))
t = int(input())
print(below_threshold(l, t))
