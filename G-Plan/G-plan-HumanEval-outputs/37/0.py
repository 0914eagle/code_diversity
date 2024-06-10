
from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    def check_below_threshold(num: int, threshold: int) -> bool:
        return num < threshold

    return all(check_below_threshold(num, t) for num in l)

# Test cases
if __name__ == "__main__":
    l = list(map(int, input().split()))
    t = int(input())
    print(below_threshold(l, t))
