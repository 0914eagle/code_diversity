
from typing import List

def remove_duplicates(l: List[int]) -> List[int]:
    unique_dict = {}
    for num in l:
        unique_dict[num] = True
    return list(unique_dict.keys())

def sort_list(l: List[int]) -> List[int]:
    return sorted(l)

def unique(l: List[int]) -> List[int]:
    unique_elements = remove_duplicates(l)
    return sort_list(unique_elements)

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = unique(input_list)
    print(result)
