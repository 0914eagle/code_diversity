
from typing import List

def incr_list(l: List[int]) -> List[int]:
    return [num + 1 for num in l]

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = incr_list(input_list)
    print(result)
