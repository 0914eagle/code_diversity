
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        indices_divisible_by_three = {i: lst[i] for i in range(len(lst)) if i % 3 == 0}
        sorted_values = [v for _, v in sorted(indices_divisible_by_three.items(), key=lambda x: x[1])]
        return sorted_values

    sorted_values = sort_values_at_indices_divisible_by_three(l)
    modified_list = [v if i % 3 != 0 else sorted_values.pop(0) for i, v in enumerate(l)]
    return modified_list

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = sort_third(input_list)
    print(result)
