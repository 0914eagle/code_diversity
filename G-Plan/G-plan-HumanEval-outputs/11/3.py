
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def check_triple_exists(nums, target):
        seen = set()
        for num in nums:
            if target - num in seen:
                return True
            seen.add(num)
        return False

    if len(l) < 3:
        return False

    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            third_element = -(l[i] + l[j])
            if check_triple_exists(l[j + 1:], third_element):
                return True

    return False

input_list = list(map(int, input().split()))
print(triples_sum_to_zero(input_list))
