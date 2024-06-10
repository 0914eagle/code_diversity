
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        sorted_values = sorted([v for i, v in enumerate(lst) if i % 3 == 0])
        return {i: v for i, v in enumerate(sorted_values) if i % 3 == 0}

    def update_list_with_sorted_values(original_list, sorted_values_dict):
        for i, v in sorted_values_dict.items():
            original_list[i] = v
        return original_list

    sorted_values_dict = sort_values_at_indices_divisible_by_three(l)
    modified_list = update_list_with_sorted_values(l.copy(), sorted_values_dict)
    return modified_list

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = sort_third(input_list)
    print(result)
