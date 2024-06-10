
from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    def find_triple_sum_to_zero(nums):
        seen = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    return True
                seen.add(nums[j])
        return False

    if len(l) < 3:
        return False

    return find_triple_sum_to_zero(l)

# Test cases
if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(triples_sum_to_zero(l))
