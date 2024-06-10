
from typing import List

def unique(l: List[int]) -> List[int]:
    return sorted(list(set(l)))

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = unique(input_list)
    print(result)
