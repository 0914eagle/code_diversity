
import sys

def solve(L, R):
    count = 0
    for i in range(L, R+1):
        num_sixes = 0
        num_eights = 0
        has_four = False
        while i > 0:
            digit = i % 10
            if digit == 4:
                has_four = True
                break
            elif digit == 6 or digit == 8:
                if digit == 6:
                    num_sixes += 1
                else:
                    num_eights += 1
            i //= 10
        if not has_four and num_sixes == num_eights:
            count += 1
    return count % (10**9+7)

L, R = map(int, input().split())
print(solve(L, R))

