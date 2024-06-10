
from typing import List

def sort_third(l: List[int]) -> List[int]:
    def sort_values_at_indices_divisible_by_three(lst):
        divisible_by_three = {i: val for i, val in enumerate(lst) if i % 3 == 0}
        sorted_values = [val for _, val in sorted(divisible_by_three.items(), key=lambda x: x[1])]
        for i, val in enumerate(sorted_values):
            lst[i * 3] = val
        return lst

    def combine_lists(lst1, lst2):
        result = []
        idx1, idx2 = 0, 0
        for i in range(len(lst1) + len(lst2)):
            if i % 3 == 0:
                result.append(lst2[idx2])
                idx2 += 1
            else:
                result.append(lst1[idx1])
                idx1 += 1
        return result

    non_divisible_by_three = [val for i, val in enumerate(l) if i % 3 != 0]
    sorted_divisible_by_three = sort_values_at_indices_divisible_by_three(l)
    result = combine_lists(non_divisible_by_three, sorted_divisible_by_three)
    return result

if __name__ == "__main__":
    l = list(map(int, input().split()))
    result = sort_third(l)
    print(result)
