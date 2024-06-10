
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        div_by_three = {i: val for i, val in enumerate(lst) if i % 3 == 0}
        sorted_values = [val for _, val in sorted(div_by_three.items(), key=lambda x: x[1])]
        for i, val in div_by_three.items():
            lst[i] = sorted_values.pop(0)
    
    sort_values_at_indices_divisible_by_three(l)
    return l

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = sort_third(input_list)
    print(result)
