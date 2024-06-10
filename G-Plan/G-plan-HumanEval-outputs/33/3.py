
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        divisible_by_three = {idx: val for idx, val in enumerate(lst) if idx % 3 == 0}
        sorted_values = [val for idx, val in sorted(divisible_by_three.items(), key=lambda x: x[1])]
        for idx, val in divisible_by_three.items():
            lst[idx] = sorted_values.pop(0)
        return lst

    return sort_values_at_indices_divisible_by_three(l)

if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = sort_third(l)
    print(result)
