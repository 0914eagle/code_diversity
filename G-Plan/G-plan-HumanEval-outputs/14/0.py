
from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    def using_set(l: List[int]) -> bool:
        seen = set()
        for num in l:
            if -num in seen:
                return True
            seen.add(num)
        return False

    def sorting_and_two_pointers(l: List[int]) -> bool:
        l.sort()
        left, right = 0, len(l) - 1
        while left < right:
            total = l[left] + l[right]
            if total == 0:
                return True
            elif total > 0:
                right -= 1
            else:
                left += 1
        return False

    return using_set(l) or sorting_and_two_pointers(l)

l = list(map(int, input().strip().split()))
print(pairs_sum_to_zero(l))
