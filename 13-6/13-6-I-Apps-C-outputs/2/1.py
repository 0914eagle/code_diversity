
import sys

def solve(L, R):
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        if '4' in num_str:
            continue
        six_count = eight_count = 0
        for digit in num_str:
            if digit == '6':
                six_count += 1
            elif digit == '8':
                eight_count += 1
        if six_count == eight_count:
            count += 1
    return count % (10**9 + 7)

L, R = map(int, input().split())
print(solve(L, R))

