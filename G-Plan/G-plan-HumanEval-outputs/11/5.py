
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def check_triple_exists(nums, target):
        seen = set()
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    complement = target - num1 - num2
                    if complement in seen:
                        return True
            seen.add(num1)
        return False

    if len(l) < 3:
        return False

    return check_triple_exists(l, 0)

# Test cases
l = input().strip().split()
l = [int(num) for num in l]
print(triples_sum_to_zero(l))
