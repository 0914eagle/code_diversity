
from typing import List

def remove_duplicates(l: List[int]) -> List[int]:
    unique_set = set(l)
    return sorted(list(unique_set))

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = remove_duplicates(input_list)
    print(result)
