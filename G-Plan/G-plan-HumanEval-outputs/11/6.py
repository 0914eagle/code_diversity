
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def find_triple_sum_to_zero(nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in seen:
                    return True
            seen.add(nums[i])
        return False

    if len(l) < 3:
        return False
    return find_triple_sum_to_zero(l)

triples_sum_to_zero([1, 3, 5, 0])
triples_sum_to_zero([1, 3, -2, 1])
triples_sum_to_zero([1, 2, 3, 7])
triples_sum_to_zero([2, 4, -5, 3, 9, 7])
triples_sum_to_zero([1])
