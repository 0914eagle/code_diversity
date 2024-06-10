
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(l: List[int]) -> List[int]:
        divisible_by_three_indices = {i: l[i] for i in range(len(l)) if i % 3 == 0}
        sorted_values = [v for _, v in sorted(divisible_by_three_indices.items())]
        return sorted_values

    def combine_lists(original_list: List[int], sorted_values: List[int]) -> List[int]:
        modified_list = original_list.copy()
        for i, v in enumerate(sorted_values):
            modified_list[i * 3] = v
        return modified_list

    sorted_values = sort_values_at_indices_divisible_by_three(l)
    modified_list = combine_lists(l, sorted_values)
    return modified_list

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = sort_third(input_list)
    print(result)
