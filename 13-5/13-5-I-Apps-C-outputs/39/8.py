
import sys

def solve(L, R):
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        if '4' in num_str:
            continue
        sixes = num_str.count('6')
        eights = num_str.count('8')
        if sixes == eights:
            count += 1
    return count % (10**9 + 7)

L, R = map(int, input().split())
print(solve(L, R))

