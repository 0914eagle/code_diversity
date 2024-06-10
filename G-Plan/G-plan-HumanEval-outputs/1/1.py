
from typing import List

def eat(number: int, need: int, remaining: int) -> List[int]:
    total_eaten = number + need
    carrots_left = remaining - need if remaining >= need else 0
    return [total_eaten, carrots_left]

if __name__ == "__main__":
    number, need, remaining = map(int, input().split())
    result = eat(number, need, remaining)
    print(result[0], result[1])
