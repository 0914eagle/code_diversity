
from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    def using_set(l: List[int]) -> bool:
        complements = set()
        for num in l:
            if -num in complements:
                return True
            complements.add(num)
        return False

    def sorting_and_two_pointers(l: List[int]) -> bool:
        l.sort()
        left, right = 0, len(l) - 1
        while left < right:
            current_sum = l[left] + l[right]
            if current_sum == 0:
                return True
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
        return False

    return using_set(l) or sorting_and_two_pointers(l)

l = list(map(int, input().split()))
print(pairs_sum_to_zero(l))
