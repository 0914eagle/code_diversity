
from typing import List

def remove_duplicates(l: List[int]) -> List[int]:
    unique_set = set(l)
    return sorted(list(unique_set))

def unique(l: List[int]) -> List[int]:
    return remove_duplicates(l)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = unique(input_list)
    print(result)
