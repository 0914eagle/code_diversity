
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def check_triple_exists(nums, target):
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement = target - nums[i] - nums[j]
                if complement in seen:
                    return True
                seen.add(nums[j])
        return False
    
    if len(l) < 3:
        return False
    
    return check_triple_exists(l, 0)

# Test cases
input_list = input().strip().split()
input_list = [int(num) for num in input_list]
print(triples_sum_to_zero(input_list))
