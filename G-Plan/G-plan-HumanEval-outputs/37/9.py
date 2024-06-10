
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    return all(num < t for num in l)

l = input().strip().split()
t = int(input().strip())
l = [int(num) for num in l]
print(below_threshold(l, t))
