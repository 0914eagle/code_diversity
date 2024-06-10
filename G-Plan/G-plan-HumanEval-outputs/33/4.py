
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        divisible_by_three = {idx: val for idx, val in enumerate(lst) if idx % 3 == 0}
        sorted_values = [val for idx, val in sorted(divisible_by_three.items(), key=lambda x: x[1])]
        return sorted_values

    def combine_lists(original_lst, sorted_lst):
        modified_lst = []
        sorted_idx = 0
        for idx, val in enumerate(original_lst):
            if idx % 3 == 0:
                modified_lst.append(sorted_lst[sorted_idx])
                sorted_idx += 1
            else:
                modified_lst.append(val)
        return modified_lst

    sorted_values = sort_values_at_indices_divisible_by_three(l)
    modified_list = combine_lists(l, sorted_values)
    return modified_list

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    result = sort_third(input_list)
    print(result)
