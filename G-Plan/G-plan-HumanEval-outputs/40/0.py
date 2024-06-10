
from typing import List

def unique(l: List[int]) -> List[int]:
    unique_dict = {}
    for num in l:
        unique_dict[num] = True
    return sorted(list(unique_dict.keys()))

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = unique(input_list)
    print(result)
