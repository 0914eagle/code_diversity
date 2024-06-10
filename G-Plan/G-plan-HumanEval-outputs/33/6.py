
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        sorted_values = sorted(lst)
        return sorted_values

    def combine_lists(lst1, lst2):
        result = []
        idx = 0
        for i in range(len(lst1)):
            if i % 3 == 0:
                result.append(lst2[idx])
                idx += 1
            else:
                result.append(lst1[i])
        return result

    values_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_values = sort_values_at_indices_divisible_by_three(values_divisible_by_three)
    modified_list = combine_lists(l, sorted_values)

    return modified_list

if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = sort_third(l)
    print(result)
