
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def find_triple_summing_to_zero(nums):
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
    return find_triple_summing_to_zero(l)

# Test cases
input_list = input().strip().split()
input_list = [int(num) for num in input_list]
print(triples_sum_to_zero(input_list))
