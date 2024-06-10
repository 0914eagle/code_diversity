
from typing import List

def get_positive(l: List[int]) -> List[int]:
    return [num for num in l if num > 0]

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = get_positive(input_list)
    print(result)
